import React, { useState } from "react";
import { Link, useNavigate, useLocation } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import Button from "../Components/Button";
import serviqLogo from "../assets/serviqlogo.png";

const Login = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const { login } = useAuth();
  const navigate = useNavigate();
  const location = useLocation();

  const from = location.state?.from?.pathname || "/";

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (!email || !password) {
      setError("Please fill in all fields.");
      return;
    }

    setLoading(true);
    const result = login(email, password);
    setLoading(false);

    if (result.success) {
      navigate(from, { replace: true });
    } else {
      setError(result.error || "Login failed. Please check credentials.");
    }
  };

  const handleUseDemo = () => {
    setEmail("demo@serviq.com");
    setPassword("password123");
    setError("");
  };

  return (
    <div className="auth-container">
      <div className="auth-card">
        {/* Brand Header */}
        <div style={{ textAlign: "center", marginBottom: "1.5rem" }}>
          <div className="brand-logo" style={{ justifyContent: "center", marginBottom: "0.6rem" }}>
            <img src={serviqLogo} alt="ServIQ" className="brand-logo-img" />
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
              value={email}
              onChange={(e) => {
                setEmail(e.target.value);
                setError("");
              }}
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
              value={password}
              onChange={(e) => {
                setPassword(e.target.value);
                setError("");
              }}
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