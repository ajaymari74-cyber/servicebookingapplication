import React from "react";
import { Link } from "react-router-dom";
import Button from "./Button";

const ServiceCard = ({ service }) => {
  return (
    <div className="service-card">
      <div className="service-card-top">
        <div className="service-emoji">{service.icon}</div>
        <span className="badge badge-blue">{service.category}</span>
      </div>

      <h3 className="service-title">{service.name}</h3>
      <p className="service-description">{service.shortDesc}</p>

      <div className="service-card-meta">
        <span className="service-rating-star">★ {service.rating}</span>
        <span>•</span>
        <span>⏱️ {service.duration}</span>
      </div>

      <div className="service-bottom-row">
        <div className="service-price-block">
          <span className="service-price-current">₹{service.price}</span>
          {service.originalPrice && (
            <span className="service-price-old">₹{service.originalPrice}</span>
          )}
        </div>

        <div style={{ display: "flex", alignItems: "center", gap: "0.6rem" }}>
          <Link
            to={`/services/${service.id}`}
            style={{ fontSize: "0.86rem", color: "var(--text-muted)", fontWeight: 600 }}
          >
            Details
          </Link>
          <Button to={`/book/${service.id}`} variant="primary" size="sm">
            Book Now
          </Button>
        </div>
      </div>
    </div>
  );
};

export default ServiceCard;
