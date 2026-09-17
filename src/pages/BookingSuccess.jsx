import React, { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { getStoredBookings } from "../utils/bookingStorage";
import Button from "../Components/Button";

const BookingSuccess = () => {
  const [searchParams] = useSearchParams();
  const bookingId = searchParams.get("id");
  const [booking, setBooking] = useState(null);

  useEffect(() => {
    const all = getStoredBookings();
    if (bookingId) {
      const found = all.find((b) => b.id === parseInt(bookingId));
      if (found) setBooking(found);
    } else if (all.length > 0) {
      setBooking(all[0]);
    }
  }, [bookingId]);

  return (
    <div className="container" style={{ padding: "2.5rem 1.25rem 4.5rem" }}>
      <div className="receipt-wrapper">
        <div className="receipt-icon">
          ✓
        </div>

        <span className="badge badge-green" style={{ marginBottom: "0.6rem" }}>
          Confirmed
        </span>

        <h1 style={{ fontSize: "1.75rem", fontWeight: 800, color: "var(--text-main)", marginBottom: "0.4rem" }}>
          Booking Confirmed!
        </h1>
        <p style={{ color: "var(--text-muted)", fontSize: "0.92rem" }}>
          We've received your request and assigned a verified technician.
        </p>

        {/* Clean Receipt Box */}
        <div className="receipt-data-box">
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", borderBottom: "1px solid var(--border)", paddingBottom: "0.75rem", marginBottom: "0.9rem" }}>
            <div>
              <span style={{ fontSize: "0.75rem", color: "var(--text-muted)", textTransform: "uppercase", fontWeight: 700 }}>Booking ID</span>
              <div style={{ fontSize: "1.1rem", fontWeight: 800, color: "var(--primary)" }}>
                #SRV-{booking ? booking.id : "10492"}
              </div>
            </div>
            <span className="badge badge-blue">
              {booking ? booking.status : "Confirmed"}
            </span>
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.9rem", fontSize: "0.88rem" }}>
            <div>
              <span style={{ color: "var(--text-muted)", fontSize: "0.78rem" }}>Service</span>
              <div style={{ fontWeight: 600, color: "var(--text-main)" }}>
                {booking ? `${booking.icon || "⚡"} ${booking.serviceName}` : "⚡ Doorstep Service"}
              </div>
            </div>

            <div>
              <span style={{ color: "var(--text-muted)", fontSize: "0.78rem" }}>Date & Time</span>
              <div style={{ fontWeight: 600, color: "var(--text-main)" }}>
                {booking ? `${booking.date} at ${booking.time}` : "Tomorrow at 11:00 AM"}
              </div>
            </div>

            <div>
              <span style={{ color: "var(--text-muted)", fontSize: "0.78rem" }}>Customer</span>
              <div style={{ fontWeight: 600, color: "var(--text-main)" }}>
                {booking ? booking.customerName : "Valued Customer"}
              </div>
            </div>

            <div>
              <span style={{ color: "var(--text-muted)", fontSize: "0.78rem" }}>Total</span>
              <div style={{ fontWeight: 700, color: "var(--success-text)", fontSize: "1rem" }}>
                ₹{booking ? booking.price : "499"}
              </div>
            </div>

            <div style={{ gridColumn: "1 / -1" }}>
              <span style={{ color: "var(--text-muted)", fontSize: "0.78rem" }}>Location</span>
              <div style={{ color: "var(--text-main)", fontSize: "0.86rem", marginTop: "0.15rem" }}>
                📍 {booking ? booking.address : "Customer Address"}
              </div>
            </div>
          </div>
        </div>

        {/* Actions */}
        <div style={{ display: "flex", gap: "0.75rem", justifyContent: "center", flexWrap: "wrap" }}>
          <Button to="/my-bookings" variant="primary">
            View in My Bookings
          </Button>
          <Button to="/services" variant="secondary">
            Book Another Service
          </Button>
          <Button to="/" variant="outline">
            Home
          </Button>
        </div>
      </div>
    </div>
  );
};

export default BookingSuccess;
