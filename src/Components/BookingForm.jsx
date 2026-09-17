import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { addBooking } from "../utils/bookingStorage";
import Button from "./Button";

const TIME_SLOTS = [
  "09:00 AM",
  "11:00 AM",
  "01:00 PM",
  "03:00 PM",
  "05:00 PM",
  "07:00 PM"
];

const BookingForm = ({ service }) => {
  const navigate = useNavigate();
  const { currentUser } = useAuth();

  const tomorrow = new Date();
  tomorrow.setDate(tomorrow.getDate() + 1);
  const defaultDateStr = tomorrow.toISOString().split("T")[0];
  const todayStr = new Date().toISOString().split("T")[0];

  const [date, setDate] = useState(defaultDateStr);
  const [time, setTime] = useState("11:00 AM");
  const [customerName, setCustomerName] = useState("");
  const [customerPhone, setCustomerPhone] = useState("");
  const [address, setAddress] = useState("");
  const [landmark, setLandmark] = useState("");
  const [notes, setNotes] = useState("");
  const [paymentMethod, setPaymentMethod] = useState("cash");
  const [error, setError] = useState("");
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    if (currentUser) {
      if (!customerName) setCustomerName(currentUser.fullName || currentUser.name || "");
      if (!customerPhone) setCustomerPhone(currentUser.phone || "");
      if (!address) setAddress(currentUser.address || "");
    }
  }, [currentUser]);

  const totalPrice = service ? service.price : 499;

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!customerName.trim() || !customerPhone.trim() || !address.trim()) {
      setError("Please fill in your name, phone, and address.");
      return;
    }

    setSubmitting(true);

    const bookingPayload = {
      serviceId: service ? service.id : 1,
      serviceName: service ? service.name : "Doorstep Service",
      icon: service ? service.icon : "⚡",
      date,
      time,
      customerName,
      customerPhone,
      address: landmark ? `${address} (Near ${landmark})` : address,
      notes,
      paymentMethod: paymentMethod === "cash" ? "Cash after Service" : "Paid Online",
      price: totalPrice
    };

    try {
      const saved = addBooking(bookingPayload);
      setTimeout(() => {
        navigate(`/booking-success?id=${saved.id}`);
      }, 300);
    } catch (err) {
      console.error(err);
      setError("Something went wrong. Please try again.");
      setSubmitting(false);
    }
  };

  return (
    <div className="booking-grid">
      {/* Left Column: Form in 3 Simple Steps */}
      <div className="booking-form-box">
        {error && (
          <div style={{ padding: "0.75rem 1rem", background: "var(--danger-bg)", color: "var(--danger-text)", borderRadius: "var(--radius-sm)", marginBottom: "1.5rem", fontSize: "0.88rem" }}>
            ⚠️ {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          {/* STEP 1: DATE & TIME */}
          <div className="form-step-header">
            <span className="step-badge">1</span>
            <span className="form-step-title">Select Date & Time</span>
          </div>

          <div className="form-group">
            <label className="form-label">Date *</label>
            <input
              type="date"
              className="form-input"
              value={date}
              min={todayStr}
              onChange={(e) => setDate(e.target.value)}
              required
            />
          </div>

          <div className="form-group" style={{ marginBottom: "2rem" }}>
            <label className="form-label">Available Time Slots *</label>
            <div className="slots-grid">
              {TIME_SLOTS.map((slot) => (
                <button
                  type="button"
                  key={slot}
                  className={`slot-item ${time === slot ? "selected" : ""}`}
                  onClick={() => setTime(slot)}
                >
                  {slot}
                </button>
              ))}
            </div>
          </div>

          {/* STEP 2: ADDRESS & CONTACT */}
          <div className="form-step-header">
            <span className="step-badge">2</span>
            <span className="form-step-title">Your Details & Location</span>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.9rem" }}>
            <div className="form-group">
              <label className="form-label">Your Name *</label>
              <input
                type="text"
                className="form-input"
                placeholder="e.g. Alex Johnson"
                value={customerName}
                onChange={(e) => {
                  setCustomerName(e.target.value);
                  setError("");
                }}
                required
              />
            </div>

            <div className="form-group">
              <label className="form-label">Phone Number *</label>
              <input
                type="tel"
                className="form-input"
                placeholder="e.g. +91 98765 43210"
                value={customerPhone}
                onChange={(e) => {
                  setCustomerPhone(e.target.value);
                  setError("");
                }}
                required
              />
            </div>
          </div>

          <div className="form-group">
            <label className="form-label">Street Address / Flat *</label>
            <textarea
              className="form-textarea"
              placeholder="e.g. Flat 302, Lakeview Apartments, 4th Cross Road"
              value={address}
              onChange={(e) => {
                setAddress(e.target.value);
                setError("");
              }}
              rows={2}
              required
            />
          </div>

          <div className="form-group" style={{ marginBottom: "2rem" }}>
            <label className="form-label">Landmark (Optional)</label>
            <input
              type="text"
              className="form-input"
              placeholder="e.g. Near City Hospital"
              value={landmark}
              onChange={(e) => setLandmark(e.target.value)}
            />
          </div>

          {/* STEP 3: PAYMENT METHOD */}
          <div className="form-step-header">
            <span className="step-badge">3</span>
            <span className="form-step-title">Payment Preference</span>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.8rem", marginBottom: "1.5rem" }}>
            <label
              style={{
                display: "flex",
                alignItems: "center",
                gap: "0.6rem",
                background: paymentMethod === "cash" ? "var(--primary-light)" : "#ffffff",
                border: `1.5px solid ${paymentMethod === "cash" ? "var(--primary)" : "var(--border)"}`,
                borderRadius: "var(--radius-sm)",
                padding: "0.75rem 0.9rem",
                cursor: "pointer",
                transition: "var(--transition)"
              }}
            >
              <input
                type="radio"
                name="paymentMethod"
                value="cash"
                checked={paymentMethod === "cash"}
                onChange={() => setPaymentMethod("cash")}
              />
              <div>
                <div style={{ fontWeight: 700, fontSize: "0.9rem", color: "var(--text-main)" }}>💵 Pay after Service</div>
                <div style={{ fontSize: "0.76rem", color: "var(--text-muted)" }}>Pay cash or UPI after work is done</div>
              </div>
            </label>

            <label
              style={{
                display: "flex",
                alignItems: "center",
                gap: "0.6rem",
                background: paymentMethod === "online" ? "var(--primary-light)" : "#ffffff",
                border: `1.5px solid ${paymentMethod === "online" ? "var(--primary)" : "var(--border)"}`,
                borderRadius: "var(--radius-sm)",
                padding: "0.75rem 0.9rem",
                cursor: "pointer",
                transition: "var(--transition)"
              }}
            >
              <input
                type="radio"
                name="paymentMethod"
                value="online"
                checked={paymentMethod === "online"}
                onChange={() => setPaymentMethod("online")}
              />
              <div>
                <div style={{ fontWeight: 700, fontSize: "0.9rem", color: "var(--text-main)" }}>💳 Pay Online</div>
                <div style={{ fontSize: "0.76rem", color: "var(--text-muted)" }}>Instant contactless checkout</div>
              </div>
            </label>
          </div>

          <Button
            type="submit"
            variant="primary"
            size="lg"
            fullWidth
            disabled={submitting}
          >
            {submitting ? "Booking..." : `Confirm Booking (₹${totalPrice})`}
          </Button>
        </form>
      </div>

      {/* Right Column: Clean Order Summary Box */}
      <div>
        <div className="summary-box">
          <h3 style={{ fontSize: "1.1rem", fontWeight: 700, marginBottom: "1rem", color: "var(--text-main)" }}>
            Booking Summary
          </h3>

          {service ? (
            <div style={{ display: "flex", gap: "0.75rem", alignItems: "center", marginBottom: "1rem", paddingBottom: "1rem", borderBottom: "1px solid var(--border)" }}>
              <div style={{ width: "42px", height: "42px", borderRadius: "8px", background: "var(--primary-light)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "1.4rem" }}>
                {service.icon}
              </div>
              <div>
                <h4 style={{ fontSize: "0.95rem", fontWeight: 700, color: "var(--text-main)" }}>{service.name}</h4>
                <p style={{ color: "var(--primary)", fontSize: "0.8rem", fontWeight: 600 }}>{service.category}</p>
              </div>
            </div>
          ) : (
            <p style={{ color: "var(--text-muted)", marginBottom: "1rem" }}>Doorstep Service</p>
          )}

          <div className="summary-line">
            <span>Date</span>
            <span style={{ fontWeight: 600, color: "var(--text-main)" }}>{date || "Not picked"}</span>
          </div>

          <div className="summary-line">
            <span>Time Slot</span>
            <span style={{ fontWeight: 600, color: "var(--text-main)" }}>{time}</span>
          </div>

          <div className="summary-line">
            <span>Service Charge</span>
            <span>₹{totalPrice}</span>
          </div>

          <div className="summary-line total-line">
            <span>Total to Pay</span>
            <span style={{ color: "var(--primary)" }}>₹{totalPrice}</span>
          </div>

          <div style={{ marginTop: "1.2rem", padding: "0.75rem", background: "var(--bg-subtle)", borderRadius: "var(--radius-sm)", fontSize: "0.8rem", color: "var(--text-muted)" }}>
            🛡️ <strong>ServIQ Promise:</strong> 100% verified technician & 30-day rework guarantee. No cancellation fees.
          </div>
        </div>
      </div>
    </div>
  );
};

export default BookingForm;