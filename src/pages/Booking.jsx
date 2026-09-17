import React, { useState, useEffect } from "react";
import { useParams, Link } from "react-router-dom";
import BookingForm from "../Components/BookingForm";
import { servicesData } from "../data/servicesData";

const Booking = () => {
  const { id } = useParams();
  const [selectedService, setSelectedService] = useState(null);

  useEffect(() => {
    if (id) {
      const found = servicesData.find((s) => s.id === parseInt(id));
      if (found) {
        setSelectedService(found);
      } else {
        setSelectedService(servicesData[0]);
      }
    } else {
      setSelectedService(servicesData[0]);
    }
  }, [id]);

  const handleServiceChange = (e) => {
    const found = servicesData.find((s) => s.id === parseInt(e.target.value));
    if (found) setSelectedService(found);
  };

  return (
    <div style={{ padding: "2rem 0 4.5rem" }}>
      <div className="container">
        {/* Simple Breadcrumb Navigation */}
        <div style={{ display: "flex", gap: "0.4rem", fontSize: "0.85rem", color: "var(--text-muted)", marginBottom: "1.2rem", alignItems: "center" }}>
          <Link to="/">Home</Link>
          <span>/</span>
          <Link to="/services">Services</Link>
          <span>/</span>
          <span style={{ color: "var(--text-main)", fontWeight: 600 }}>Booking</span>
        </div>

        {/* Header and Service Switcher */}
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", flexWrap: "wrap", gap: "1rem", marginBottom: "1.5rem" }}>
          <div>
            <h1 className="page-title">Schedule an Appointment</h1>
            <p className="page-subtitle" style={{ marginTop: "0.2rem" }}>
              Select a date, time, and service location.
            </p>
          </div>

          <div style={{ display: "flex", alignItems: "center", gap: "0.6rem" }}>
            <label style={{ fontSize: "0.88rem", color: "var(--text-muted)", fontWeight: 600 }}>
              Service:
            </label>
            <select
              className="form-select"
              style={{ width: "auto", minWidth: "220px", padding: "0.5rem 0.8rem" }}
              value={selectedService ? selectedService.id : ""}
              onChange={handleServiceChange}
            >
              {servicesData.map((s) => (
                <option key={s.id} value={s.id}>
                  {s.icon} {s.name} (₹{s.price})
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Simple Booking Form */}
        {selectedService && <BookingForm service={selectedService} />}
      </div>
    </div>
  );
};

export default Booking;