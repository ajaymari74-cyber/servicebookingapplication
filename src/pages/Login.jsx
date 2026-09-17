import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import Button from "../Components/Button";

function Login() {
  const navigate = useNavigate();
  const { login } = useAuth();

  const [formData, setFormData] = useState({
    email: "",
    password: ""
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
    setError("");
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!formData.email || !formData.password) {
      setError("Please enter your email and password.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const res = await login(formData.email, formData.password);
      if (res.success) {
        navigate("/");
      } else {
        setError(res.message || "Invalid credentials.");
        setLoading(false);
      }
    } catch (err) {
      setError("An unexpected login error occurred. Please try again.");
      setLoading(false);
    }
  };

  const handleUseDemo = () => {
    setFormData({
      email: "demo@serviq.com",
      password: "password123"
    });
    setError("");
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        {/* Brand Header */}
        <div style={{ textAlign: "center", marginBottom: "1.5rem" }}>
          <div className="brand-logo" style={{ justifyContent: "center", marginBottom: "0.6rem" }}>
            <div className="brand-icon">⚡</div>
            <span>Serv<span className="text-iq">IQ</span></span>
          </div>
          <h1 style={{ fontSize: "1.45rem", fontWeight: 800, color: "var(--text-main)", marginBottom: "0.25rem" }}>
            Sign In
          </h1>
          <p style={{ fontSize: "0.88rem", color: "var(--text-muted)" }}>
            Access your bookings and appointments
          </p>
        </div>

        {/* 1-Click Demo Button */}
        <div style={{ marginBottom: "1.2rem", padding: "0.75rem", background: "var(--bg-subtle)", border: "1px solid var(--border)", borderRadius: "var(--radius-sm)", display: "flex", alignItems: "center", justifyContent: "space-between" }}>
          <span style={{ fontSize: "0.82rem", color: "var(--text-muted)" }}>Testing the app?</span>
          <Button
            type="button"
            variant="secondary"
            size="sm"
            onClick={handleUseDemo}
          >
            Fill Demo Login
          </Button>
        </div>

        {error && (
          <div style={{ padding: "0.65rem 0.85rem", background: "var(--danger-bg)", color: "var(--danger-text)", borderRadius: "var(--radius-sm)", marginBottom: "1.2rem", fontSize: "0.86rem" }}>
            ⚠️ {error}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label">Email</label>
            <input
              type="email"
              name="email"
              className="form-input"
              placeholder="e.g. demo@serviq.com"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </div>

          <div className="form-group">
            <label className="form-label">Password</label>
            <input
              type="password"
              name="password"
              className="form-input"
              placeholder="Enter your password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </div>

          <Button
            type="submit"
            variant="primary"
            size="lg"
            fullWidth
            style={{ marginTop: "0.8rem" }}
            disabled={loading}
          >
            {loading ? "Signing in..." : "Sign In"}
          </Button>
        </form>

        <p style={{ textAlign: "center", marginTop: "1.4rem", fontSize: "0.86rem", color: "var(--text-muted)" }}>
          Don't have an account?{" "}
          <Link to="/register" style={{ color: "var(--primary)", fontWeight: 700 }}>
            Register here
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Login;