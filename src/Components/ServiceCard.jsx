import React from "react";
import { Link } from "react-router-dom";
import Button from "./Button";

const ServiceCard = ({ service }) => {
  return (
    <div className="service-card">
      <Link to={`/services/${service.id}`} className="service-card-image-wrap">
        {service.image ? (
          <img
            src={service.image}
            alt={service.name}
            className="service-card-image"
            loading="lazy"
          />
        ) : (
          <div className="service-card-placeholder">
            <span style={{ fontSize: "2.5rem" }}>{service.icon}</span>
          </div>
        )}

        <div className="service-card-badges-row">
          <span className="badge badge-blue service-card-tag">
            {service.category}
          </span>
          {service.badge && (
            <span className="service-card-badge-special">
              {service.badge}
            </span>
          )}
        </div>
      </Link>

      <div className="service-card-body">
        <div className="service-card-header">
          <span className="service-mini-icon">{service.icon}</span>
          <h3 className="service-title">
            <Link to={`/services/${service.id}`} className="service-title-link">
              {service.name}
            </Link>
          </h3>
        </div>

        <p className="service-description">{service.shortDesc}</p>

        <div className="service-card-meta">
          <span className="service-rating-star">★ {service.rating}</span>
          <span className="service-meta-reviews">({service.reviewsCount || 100}+)</span>
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
              className="service-details-link"
            >
              Details
            </Link>
            <Button to={`/book/${service.id}`} variant="primary" size="sm">
              Book Now
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ServiceCard;

