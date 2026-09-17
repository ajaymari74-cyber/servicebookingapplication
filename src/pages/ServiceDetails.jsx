import React from "react";
import { useParams, Link, useNavigate } from "react-router-dom";
import { servicesData } from "../data/servicesData";
import ServiceCard from "../Components/ServiceCard";
import Button from "../Components/Button";

const ServiceDetails = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const service = servicesData.find((s) => s.id === parseInt(id));
  const [activeImage, setActiveImage] = React.useState(service?.image || null);

  React.useEffect(() => {
    if (service) {
      setActiveImage(service.image);
    }
  }, [service]);

  if (!service) {
    return (
      <div className="container" style={{ padding: "5rem 1.25rem", textAlign: "center" }}>
        <h2 style={{ fontSize: "1.8rem", fontWeight: 700, marginBottom: "0.5rem" }}>Service Not Found</h2>
        <p style={{ color: "var(--text-muted)", marginBottom: "1.5rem" }}>
          The requested service could not be found.
        </p>
        <Button to="/services" variant="primary">
          View All Services
        </Button>
      </div>
    );
  }

  const relatedServices = servicesData
    .filter((s) => s.id !== service.id && s.category === service.category)
    .slice(0, 3);

  const galleryImages = service.gallery || (service.image ? [service.image] : []);

  return (
    <div style={{ padding: "2rem 0 4.5rem" }}>
      <div className="container">
        {/* Simple Breadcrumb */}
        <div style={{ display: "flex", gap: "0.4rem", fontSize: "0.85rem", color: "var(--text-muted)", marginBottom: "1.5rem", alignItems: "center" }}>
          <Link to="/">Home</Link>
          <span>/</span>
          <Link to="/services">Services</Link>
          <span>/</span>
          <span style={{ color: "var(--text-main)", fontWeight: 600 }}>{service.name}</span>
        </div>

        {/* 2-Column Details Layout */}
        <div style={{ display: "grid", gridTemplateColumns: "1.6fr 1fr", gap: "2.2rem", alignItems: "start" }}>
          {/* Main Info */}
          <div>
            {/* Service Featured Image Banner */}
            {activeImage && (
              <div className="service-details-banner-container">
                <img
                  src={activeImage}
                  alt={service.name}
                  className="service-details-banner-img"
                />
                <div className="service-details-banner-badge">
                  <span className="badge badge-blue">{service.category}</span>
                  {service.badge && (
                    <span className="service-card-badge-special">{service.badge}</span>
                  )}
                </div>
              </div>
            )}

            {/* Gallery Thumbnails (if multiple images like Pest Control) */}
            {galleryImages.length > 1 && (
              <div className="service-details-gallery-row">
                {galleryImages.map((imgSrc, idx) => (
                  <button
                    key={idx}
                    type="button"
                    className={`gallery-thumb-btn ${activeImage === imgSrc ? "active" : ""}`}
                    onClick={() => setActiveImage(imgSrc)}
                  >
                    <img src={imgSrc} alt={`${service.name} view ${idx + 1}`} />
                  </button>
                ))}
              </div>
            )}

            <div style={{ display: "flex", alignItems: "center", gap: "0.9rem", margin: "1.2rem 0 0.6rem" }}>
              <div style={{ width: "48px", height: "48px", borderRadius: "12px", background: "var(--primary-light)", display: "flex", alignItems: "center", justifyContent: "center", fontSize: "1.6rem", flexShrink: 0 }}>
                {service.icon}
              </div>
              <div>
                <span className="badge badge-blue" style={{ marginBottom: "0.2rem" }}>
                  {service.category}
                </span>
                <h1 style={{ fontSize: "1.85rem", fontWeight: 800, color: "var(--text-main)", lineHeight: "1.2" }}>
                  {service.name}
                </h1>
              </div>
            </div>

            <div style={{ display: "flex", gap: "1rem", color: "var(--text-muted)", fontSize: "0.9rem", margin: "0.8rem 0 1.2rem", alignItems: "center" }}>
              <span style={{ color: "#d97706", fontWeight: 700 }}>★ {service.rating} ({service.reviewsCount} reviews)</span>
              <span>•</span>
              <span>⏱️ {service.duration}</span>
              <span>•</span>
              <span style={{ color: "var(--success-text)", fontWeight: 600 }}>✓ Certified Expert</span>
            </div>

            <p style={{ fontSize: "0.96rem", lineHeight: "1.6", color: "var(--text-muted)", marginBottom: "1.8rem" }}>
              {service.description}
            </p>

            {/* What's Included */}
            <div style={{ background: "#ffffff", border: "1px solid var(--border)", borderRadius: "var(--radius-md)", padding: "1.6rem", marginBottom: "1.5rem" }}>
              <h3 style={{ fontSize: "1.1rem", fontWeight: 700, marginBottom: "0.9rem", color: "var(--text-main)" }}>
                What's Included in this Service
              </h3>
              <div style={{ display: "flex", flexDirection: "column", gap: "0.6rem" }}>
                {service.included && service.included.map((inc, i) => (
                  <div key={i} style={{ display: "flex", alignItems: "flex-start", gap: "0.5rem" }}>
                    <span style={{ color: "var(--success)", fontWeight: 700 }}>✓</span>
                    <span style={{ fontSize: "0.92rem", color: "var(--text-main)" }}>{inc}</span>
                  </div>
                ))}
              </div>
            </div>

            {/* Guarantees */}
            <div style={{ background: "#ffffff", border: "1px solid var(--border)", borderRadius: "var(--radius-md)", padding: "1.6rem" }}>
              <h3 style={{ fontSize: "1.1rem", fontWeight: 700, marginBottom: "0.9rem", color: "var(--text-main)" }}>
                ServIQ Service Promise
              </h3>
              <div style={{ display: "flex", flexDirection: "column", gap: "0.6rem" }}>
                {service.features && service.features.map((feat, i) => (
                  <div key={i} style={{ display: "flex", alignItems: "center", gap: "0.5rem", fontSize: "0.92rem" }}>
                    <span>⭐</span>
                    <span style={{ color: "var(--text-main)" }}>{feat}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Sticky Booking Sidebar */}
          <div style={{ position: "sticky", top: "80px" }}>
            <div className="summary-box">
              {service.image && (
                <div style={{ marginBottom: "1.1rem", borderRadius: "var(--radius-sm)", overflow: "hidden", height: "130px", border: "1px solid var(--border)" }}>
                  <img
                    src={service.image}
                    alt={service.name}
                    style={{ width: "100%", height: "100%", objectFit: "cover" }}
                  />
                </div>
              )}
              <span className="badge badge-blue" style={{ marginBottom: "0.5rem" }}>
                Fixed Price
              </span>

              <div style={{ display: "flex", alignItems: "baseline", gap: "0.6rem", margin: "0.4rem 0 0.8rem" }}>
                <span style={{ fontSize: "2rem", fontWeight: 800, color: "var(--primary)" }}>
                  ₹{service.price}
                </span>
                {service.originalPrice && (
                  <span style={{ fontSize: "1rem", color: "var(--text-light)", textDecoration: "line-through" }}>
                    ₹{service.originalPrice}
                  </span>
                )}
              </div>

              <p style={{ fontSize: "0.86rem", color: "var(--text-muted)", marginBottom: "1.2rem" }}>
                Standard diagnostic, labor & inspection included. Pay after completion.
              </p>

              <Button
                onClick={() => navigate(`/book/${service.id}`)}
                variant="primary"
                size="lg"
                fullWidth
                style={{ marginBottom: "1rem" }}
              >
                Book Now (Pick Time Slot) →
              </Button>

              <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem", fontSize: "0.82rem", color: "var(--text-muted)", borderTop: "1px solid var(--border)", paddingTop: "1rem" }}>
                <div>🛡️ <strong>30-Day Guarantee:</strong> Free rework if unsatisfied</div>
                <div>⚡ <strong>Quick Arrival:</strong> Technician allocated on time</div>
                <div>💳 <strong>Safe Pay:</strong> Cash or UPI after service</div>
              </div>
            </div>
          </div>
        </div>

        {/* Related Services */}
        {relatedServices.length > 0 && (
          <div style={{ marginTop: "4rem", borderTop: "1px solid var(--border)", paddingTop: "2rem" }}>
            <h2 className="section-title" style={{ marginBottom: "1.2rem" }}>
              Related Services
            </h2>
            <div className="services-grid">
              {relatedServices.map((rel) => (
                <ServiceCard key={rel.id} service={rel} />
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ServiceDetails;
