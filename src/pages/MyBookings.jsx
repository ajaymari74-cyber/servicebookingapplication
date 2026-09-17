import React, { useEffect, useState } from "react";
import { getStoredBookings, cancelBookingById } from "../utils/bookingStorage";
import { servicesData } from "../data/servicesData";
import Button from "../Components/Button";

export const MyBookings = () => {
  const [bookings, setBookings] = useState([]);
  const [activeTab, setActiveTab] = useState("All");
  const [cancelModalBooking, setCancelModalBooking] = useState(null);

  useEffect(() => {
    setBookings(getStoredBookings());
  }, []);

  const handleConfirmCancel = () => {
    if (cancelModalBooking) {
      const updated = cancelBookingById(cancelModalBooking.id);
      setBookings(updated);
      setCancelModalBooking(null);
    }
  };

  const filteredBookings = bookings.filter((b) => {
    if (activeTab === "All") return true;
    return b.status.toLowerCase() === activeTab.toLowerCase();
  });

  const getStatusBadge = (status) => {
    switch (status) {
      case "Confirmed":
        return <span className="badge badge-blue">Confirmed</span>;
      case "Completed":
        return <span className="badge badge-green">Completed</span>;
      case "Cancelled":
        return <span className="badge badge-red">Cancelled</span>;
      default:
        return <span className="badge badge-orange">{status}</span>;
    }
  };

  return (
    <div style={{ padding: "2.5rem 0 4.5rem" }}>
      <div className="container">
        {/* Header */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "flex-end", marginBottom: "1.8rem", flexWrap: "wrap", gap: "1rem" }}>
          <div>
            <h1 className="page-title">My Bookings</h1>
            <p className="page-subtitle" style={{ marginTop: "0.2rem" }}>
              View and manage your scheduled doorstep service appointments.
            </p>
          </div>

          <Button to="/services" variant="primary" size="sm">
            + Book New Service
          </Button>
        </div>

        {/* Tab Filters */}
        <div className="tabs-bar">
          {["All", "Confirmed", "Completed", "Cancelled"].map((tab) => {
            const count = bookings.filter((b) => tab === "All" ? true : b.status.toLowerCase() === tab.toLowerCase()).length;
            return (
              <button
                key={tab}
                className={`tab-btn ${activeTab === tab ? "active" : ""}`}
                onClick={() => setActiveTab(tab)}
              >
                {tab} ({count})
              </button>
            );
          })}
        </div>

        {/* Bookings List */}
        {filteredBookings.length > 0 ? (
          <div>
            {filteredBookings.map((b) => {
              const matchedService = servicesData.find(
                (s) => s.id === b.serviceId || s.name.toLowerCase() === (b.serviceName || "").toLowerCase()
              );
              const serviceImg = b.image || matchedService?.image;

              return (
                <div key={b.id} className="booking-card">
                  {/* Left: Image & Service Details */}
                  <div style={{ display: "flex", alignItems: "center", gap: "1rem", flex: 1 }}>
                    {serviceImg ? (
                      <img
                        src={serviceImg}
                        alt={b.serviceName}
                        style={{
                          width: "56px",
                          height: "56px",
                          borderRadius: "10px",
                          objectFit: "cover",
                          border: "1px solid var(--border)",
                          flexShrink: 0
                        }}
                      />
                    ) : (
                      <div style={{ width: "46px", height: "46px", borderRadius: "10px", background: "var(--primary-light)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "1.6rem", flexShrink: 0 }}>
                        {b.icon || "🛠️"}
                      </div>
                    )}
                    <div>
                      <div style={{ display: "flex", alignItems: "center", gap: "0.5rem", marginBottom: "0.2rem", flexWrap: "wrap" }}>
                        <h3 style={{ fontSize: "1.05rem", fontWeight: 700, color: "var(--text-main)" }}>
                          {b.serviceName}
                        </h3>
                        {getStatusBadge(b.status)}
                      </div>
                      <p style={{ color: "var(--text-muted)", fontSize: "0.82rem" }}>
                        Booking #{b.id} • 📍 {b.address}
                      </p>
                    </div>
                  </div>

                {/* Center: Appointment Time */}
                <div style={{ minWidth: "150px" }}>
                  <div style={{ fontSize: "0.78rem", color: "var(--text-muted)", textTransform: "uppercase", fontWeight: 600 }}>Scheduled</div>
                  <div style={{ fontWeight: 700, color: "var(--text-main)", fontSize: "0.92rem", marginTop: "0.15rem" }}>
                    📅 {b.date}
                  </div>
                  <div style={{ color: "var(--primary)", fontSize: "0.86rem", fontWeight: 600 }}>
                    ⏰ {b.time}
                  </div>
                </div>

                {/* Price */}
                <div style={{ minWidth: "90px" }}>
                  <div style={{ fontSize: "0.78rem", color: "var(--text-muted)", textTransform: "uppercase", fontWeight: 600 }}>Total</div>
                  <div style={{ fontSize: "1.15rem", fontWeight: 800, color: "var(--success-text)", marginTop: "0.15rem" }}>
                    ₹{b.price}
                  </div>
                </div>

                {/* Actions */}
                <div style={{ display: "flex", gap: "0.5rem" }}>
                  {b.status === "Confirmed" && (
                    <Button
                      variant="danger"
                      size="sm"
                      onClick={() => setCancelModalBooking(b)}
                    >
                      Cancel
                    </Button>
                  )}
                  <Button
                    to={`/book/${b.serviceId || 1}`}
                    variant="secondary"
                    size="sm"
                  >
                    Book Again
                  </Button>
                </div>
              </div>
            );
          })}
        </div>
        ) : (
          <div style={{ textAlign: "center", padding: "3.5rem 1.25rem", background: "#ffffff", borderRadius: "var(--radius-md)", border: "1px solid var(--border)" }}>
            <div style={{ fontSize: "2.5rem", marginBottom: "0.6rem" }}>📅</div>
            <h3 style={{ fontSize: "1.2rem", fontWeight: 700, marginBottom: "0.3rem" }}>
              No {activeTab === "All" ? "" : activeTab} Bookings
            </h3>
            <p style={{ color: "var(--text-muted)", marginBottom: "1.2rem", fontSize: "0.9rem" }}>
              You don't have any appointments in this list.
            </p>
            <Button to="/services" variant="primary">
              Book a Service
            </Button>
          </div>
        )}
      </div>

      {/* Cancellation Confirmation Modal */}
      {cancelModalBooking && (
        <div className="modal-overlay">
          <div className="modal-box">
            <h3 style={{ fontSize: "1.25rem", fontWeight: 700, marginBottom: "0.5rem", color: "var(--text-main)" }}>
              Cancel Appointment?
            </h3>
            <p style={{ color: "var(--text-muted)", fontSize: "0.9rem", marginBottom: "1.5rem", lineHeight: "1.5" }}>
              Are you sure you want to cancel your appointment for <strong>{cancelModalBooking.serviceName}</strong> on <strong>{cancelModalBooking.date}</strong> at <strong>{cancelModalBooking.time}</strong>?
            </p>
            <div style={{ display: "flex", gap: "0.75rem", justifyContent: "flex-end" }}>
              <Button
                variant="secondary"
                size="sm"
                onClick={() => setCancelModalBooking(null)}
              >
                Keep Booking
              </Button>
              <Button
                variant="danger"
                size="sm"
                onClick={handleConfirmCancel}
              >
                Yes, Cancel
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default MyBookings;