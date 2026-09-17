import React, { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import ServiceCard from "../Components/ServiceCard";
import Button from "../Components/Button";
import { servicesData, serviceCategories } from "../data/servicesData";

function Home() {
  const [search, setSearch] = useState("");
  const navigate = useNavigate();

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    if (search.trim()) {
      navigate(`/services?q=${encodeURIComponent(search.trim())}`);
    } else {
      navigate("/services");
    }
  };

  const popularServices = servicesData.slice(0, 6);

  return (
    <div>
      {/* Friendly Hero Section */}
      <section className="hero">
        <div className="container">
          <div className="hero-tag">
            ✨ Fast & Trusted Home Services
          </div>

          <h1 className="hero-title">
            Reliable home services, delivered to your door.
          </h1>

          <p className="hero-desc">
            Book verified electricians, plumbers, cleaners, and AC technicians in just a few clicks.
          </p>

          {/* Simple Search Bar */}
          <form onSubmit={handleSearchSubmit} className="hero-search">
            <span style={{ fontSize: "1rem", marginRight: "0.4rem" }}>🔍</span>
            <input
              type="text"
              placeholder="What do you need help with? (e.g. Electrician, AC repair...)"
              value={search}
              onChange={(e) => setSearch(e.target.value)}
            />
            <Button type="submit" variant="primary" size="sm">
              Search
            </Button>
          </form>

          {/* Quick Category Buttons */}
          <div className="category-pills-row">
            {serviceCategories.filter(c => c !== "All").slice(0, 5).map((cat) => (
              <Link
                key={cat}
                to={`/services?cat=${encodeURIComponent(cat)}`}
                className="pill-btn"
              >
                {cat}
              </Link>
            ))}
          </div>
        </div>
      </section>

      {/* Popular Services Section */}
      <section style={{ padding: "3.5rem 0" }}>
        <div className="container">
          <div style={{ display: "flex", alignItems: "flex-end", justifyContent: "space-between", marginBottom: "1.8rem", flexWrap: "wrap", gap: "0.75rem" }}>
            <div>
              <h2 className="section-title">Popular Services</h2>
              <p className="page-subtitle" style={{ marginTop: "0.2rem" }}>
                Our most requested doorstep repair and maintenance solutions.
              </p>
            </div>
            <Button to="/services" variant="outline" size="sm">
              View All Services ({servicesData.length}) →
            </Button>
          </div>

          <div className="services-grid">
            {popularServices.map((service) => (
              <ServiceCard key={service.id} service={service} />
            ))}
          </div>
        </div>
      </section>

      {/* How It Works (3 Clear Steps) */}
      <section className="steps-section">
        <div className="container">
          <div style={{ textAlign: "center", maxWidth: "500px", margin: "0 auto" }}>
            <h2 className="section-title">How It Works</h2>
            <p className="page-subtitle">Simple, transparent, and completely hassle-free.</p>
          </div>

          <div className="steps-grid">
            <div className="step-box">
              <div className="step-num">1</div>
              <h3 className="step-title">Choose a Service</h3>
              <p className="step-desc">Pick from our clear catalog of home repairs with upfront, fixed pricing.</p>
            </div>

            <div className="step-box">
              <div className="step-num">2</div>
              <h3 className="step-title">Pick Date & Time</h3>
              <p className="step-desc">Select a convenient schedule. Receive immediate appointment confirmation.</p>
            </div>

            <div className="step-box">
              <div className="step-num">3</div>
              <h3 className="step-title">Pay After Service</h3>
              <p className="step-desc">Our verified technician completes the job. Pay cash or online only when satisfied.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Why ServIQ (3 Core Benefits) */}
      <section style={{ padding: "3.5rem 0" }}>
        <div className="container">
          <div style={{ textAlign: "center", maxWidth: "500px", margin: "0 auto" }}>
            <h2 className="section-title">Why Homeowners Trust Us</h2>
            <p className="page-subtitle">Quality service guaranteed every single time.</p>
          </div>

          <div className="features-grid">
            <div className="feature-box">
              <div className="feature-icon">🛡️</div>
              <h3 className="feature-title">Verified Professionals</h3>
              <p className="feature-desc">All technicians undergo strict criminal background and skill checks.</p>
            </div>

            <div className="feature-box">
              <div className="feature-icon">🏷️</div>
              <h3 className="feature-title">Transparent Pricing</h3>
              <p className="feature-desc">No hidden charges or surprise diagnostic fees. What you see is what you pay.</p>
            </div>

            <div className="feature-box">
              <div className="feature-icon">⭐</div>
              <h3 className="feature-title">30-Day Guarantee</h3>
              <p className="feature-desc">If you aren't 100% satisfied, we revisit and re-service free of charge.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Clean Call To Action */}
      <section style={{ padding: "2.5rem 0 4rem" }}>
        <div className="container">
          <div
            style={{
              background: "var(--primary-light)",
              border: "1px solid #bfdbfe",
              borderRadius: "var(--radius-lg)",
              padding: "2.8rem 1.5rem",
              textAlign: "center"
            }}
          >
            <h2 style={{ fontSize: "1.8rem", fontWeight: 800, color: "var(--text-main)", marginBottom: "0.5rem" }}>
              Ready to book a service?
            </h2>
            <p style={{ color: "var(--text-muted)", maxWidth: "480px", margin: "0 auto 1.5rem", fontSize: "0.95rem" }}>
              Appointments take less than a minute. No upfront payment required.
            </p>
            <Button to="/services" variant="primary" size="lg">
              Explore All Services Now
            </Button>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;