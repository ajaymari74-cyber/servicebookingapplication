import React from "react";
import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer className="footer">
      <div className="container">
        <div className="footer-grid">
          {/* Brand Info */}
          <div>
            <div className="brand-logo" style={{ marginBottom: "0.75rem" }}>
              <div className="brand-icon">⚡</div>
              <span>Serv<span className="text-iq">IQ</span></span>
            </div>
            <p style={{ color: "var(--text-muted)", fontSize: "0.88rem", lineHeight: "1.6", maxWidth: "300px" }}>
              On-demand doorstep repair and maintenance services by certified background-verified professionals.
            </p>
          </div>

          {/* Popular Services */}
          <div>
            <h4 className="footer-title">Services</h4>
            <ul className="footer-list">
              <li><Link to="/services">Electrician</Link></li>
              <li><Link to="/services">Plumber</Link></li>
              <li><Link to="/services">AC Service</Link></li>
              <li><Link to="/services">Home Cleaning</Link></li>
              <li><Link to="/services">Carpentry</Link></li>
            </ul>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="footer-title">Company</h4>
            <ul className="footer-list">
              <li><Link to="/">Home</Link></li>
              <li><Link to="/services">All Services</Link></li>
              <li><Link to="/my-bookings">My Bookings</Link></li>
              <li><Link to="/login">Sign In</Link></li>
              <li><Link to="/register">Register</Link></li>
            </ul>
          </div>

          {/* Contact & Support */}
          <div>
            <h4 className="footer-title">Help & Support</h4>
            <p style={{ color: "var(--text-muted)", fontSize: "0.86rem", marginBottom: "0.4rem" }}>
              Available 8:00 AM – 8:00 PM daily
            </p>
            <p style={{ color: "var(--text-main)", fontWeight: 700, fontSize: "0.9rem", marginBottom: "0.2rem" }}>
              📞 1800-420-SERV
            </p>
            <p style={{ color: "var(--text-muted)", fontSize: "0.86rem" }}>
              ✉️ help@serviq.com
            </p>
          </div>
        </div>

        <div className="footer-bottom">
          <p>© {new Date().getFullYear()} ServIQ Technologies. All rights reserved.</p>
          <div style={{ display: "flex", gap: "1.2rem" }}>
            <span>Privacy</span>
            <span>Terms</span>
            <span>Support</span>
          </div>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
