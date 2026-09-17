import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import Button from "../Components/Button";
import serviqLogo from "../assets/serviqlogo.png";

export function Register() {
  const navigate = useNavigate();
  const { register, apiUrl, updateApiUrl } = useAuth();

  const [formData, setFormData] = useState({
    fullName: "",
    email: "",
    password: "",
    confirmPassword: "",
    phone: "",
    address: ""
  });

  const [error, setError] = useState("");
  const [successMsg, setSuccessMsg] = useState("");
  const [loading, setLoading] = useState(false);
  const [showApiConfig, setShowApiConfig] = useState(false);
  const [customUrlInput, setCustomUrlInput] = useState(apiUrl || "");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
    setError("");
  };

  const handleSaveApiUrl = (e) => {
    e.preventDefault();
    updateApiUrl(customUrlInput);
    setShowApiConfig(false);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const { fullName, email, phone, password, confirmPassword } = formData;

    if (!fullName || !email || !phone || !password || !confirmPassword) {
      setError("Please fill in all required fields.");
      return;
    }

    if (password.length < 6) {
      setError("Password must be at least 6 characters.");
      return;
    }

    if (password !== confirmPassword) {
      setError("Passwords do not match.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const res = await register(formData);
      if (res.success) {
        setSuccessMsg(
          res.source === "mockapi"
            ? "Account created & synced with MockAPI!"
            : "Account created successfully!"
        );
        setTimeout(() => {
          navigate("/");
        }, 1000);
      } else {
        setError(res.message || "Registration failed.");
        setLoading(false);
      }
    } catch (err) {
      setError("An unexpected error occurred. Please try again.");
      setLoading(false);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-card" style={{ maxWidth: "480px" }}>
        {/* Brand Header */}
        <div style={{ textAlign: "center", marginBottom: "1.4rem" }}>
          <div className="brand-logo" style={{ justifyContent: "center", marginBottom: "0.6rem" }}>
            <img src={serviqLogo} alt="ServIQ" className="brand-logo-img" />
            <span>Serv<span className="text-iq">IQ</span></span>
          </div>
          <h1 style={{ fontSize: "1.45rem", fontWeight: 800, color: "var(--text-main)", marginBottom: "0.25rem" }}>
            Create Account
          </h1>
          <p style={{ fontSize: "0.88rem", color: "var(--text-muted)" }}>
            Book faster and manage all your appointments
          </p>
        </div>

        {/* MockAPI Connection Badge */}
        <div style={{
          marginBottom: "1.1rem",
          padding: "0.6rem 0.8rem",
          background: "rgba(59, 130, 246, 0.08)",
          border: "1px solid rgba(59, 130, 246, 0.2)",
          borderRadius: "var(--radius-sm)",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          fontSize: "0.78rem"
        }}>
          <div style={{ display: "flex", alignItems: "center", gap: "0.4rem", overflow: "hidden", textOverflow: "ellipsis" }}>
            <span style={{ display: "inline-block", width: "8px", height: "8px", borderRadius: "50%", background: "#10b981" }}></span>
            <span style={{ color: "var(--text-muted)" }}>Mock API:</span>
            <span style={{ fontWeight: 600, color: "var(--text-main)", maxWidth: "190px", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
              {apiUrl || "MockAPI linked"}
            </span>
          </div>
          <button
            type="button"
            onClick={() => setShowApiConfig(!showApiConfig)}
            style={{
              background: "none",
              border: "none",
              color: "var(--primary)",
              fontWeight: 600,
              cursor: "pointer",
              fontSize: "0.78rem",
              padding: "2px 6px"
            }}
          >
            {showApiConfig ? "Close" : "Change URL"}
          </button>
        </div>

        {showApiConfig && (
          <form onSubmit={handleSaveApiUrl} style={{ marginBottom: "1.2rem", padding: "0.8rem", background: "var(--bg-subtle)", borderRadius: "var(--radius-sm)", border: "1px solid var(--border)" }}>
            <label className="form-label" style={{ fontSize: "0.78rem", marginBottom: "0.3rem" }}>
              MockAPI Endpoint URL
            </label>
            <div style={{ display: "flex", gap: "0.5rem" }}>
              <input
                type="url"
                value={customUrlInput}
                onChange={(e) => setCustomUrlInput(e.target.value)}
                placeholder="https://...mockapi.io/users"
                className="form-input"
                style={{ fontSize: "0.8rem", padding: "0.45rem 0.6rem" }}
              />
              <Button type="submit" variant="primary" size="sm">
                Save
              </Button>
            </div>
            <p style={{ fontSize: "0.72rem", color: "var(--text-muted)", marginTop: "0.4rem", marginBottom: 0 }}>
              Paste your cloned MockAPI endpoint here if you cloned it in your MockAPI dashboard.
            </p>
          </form>
        )}

        {error && (
          <div style={{ padding: "0.65rem 0.85rem", background: "var(--danger-bg)", color: "var(--danger-text)", borderRadius: "var(--radius-sm)", marginBottom: "1.2rem", fontSize: "0.86rem" }}>
            ⚠️ {error}
          </div>
        )}

        {successMsg && (
          <div style={{ padding: "0.65rem 0.85rem", background: "rgba(16, 185, 129, 0.12)", color: "#10b981", borderRadius: "var(--radius-sm)", marginBottom: "1.2rem", fontSize: "0.86rem", fontWeight: 600 }}>
            ✅ {successMsg}
          </div>
        )}

        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label className="form-label">Full Name *</label>
            <input
              type="text"
              name="fullName"
              className="form-input"
              placeholder="e.g. Alex Johnson"
              value={formData.fullName}
              onChange={handleChange}
              required
            />
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.8rem" }}>
            <div className="form-group">
              <label className="form-label">Email Address *</label>
              <input
                type="email"
                name="email"
                className="form-input"
                placeholder="name@example.com"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label className="form-label">Phone Number *</label>
              <input
                type="tel"
                name="phone"
                className="form-input"
                placeholder="+91 98765 43210"
                value={formData.phone}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <div className="form-group">
            <label className="form-label">Address (Optional)</label>
            <input
              type="text"
              name="address"
              className="form-input"
              placeholder="e.g. Flat 104, Green Heights"
              value={formData.address}
              onChange={handleChange}
            />
          </div>

          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: "0.8rem" }}>
            <div className="form-group">
              <label className="form-label">Password *</label>
              <input
                type="password"
                name="password"
                className="form-input"
                placeholder="Min 6 chars"
                value={formData.password}
                onChange={handleChange}
                required
              />
            </div>

            <div className="form-group">
              <label className="form-label">Confirm Password *</label>
              <input
                type="password"
                name="confirmPassword"
                className="form-input"
                placeholder="Re-enter password"
                value={formData.confirmPassword}
                onChange={handleChange}
                required
              />
            </div>
          </div>

          <Button
            type="submit"
            variant="primary"
            size="lg"
            fullWidth
            style={{ marginTop: "0.8rem" }}
            disabled={loading}
          >
            {loading ? "Creating Account..." : "Create Account"}
          </Button>
        </form>

        <p style={{ textAlign: "center", marginTop: "1.4rem", fontSize: "0.86rem", color: "var(--text-muted)" }}>
          Already have an account?{" "}
          <Link to="/login" style={{ color: "var(--primary)", fontWeight: 700 }}>
            Sign In here
          </Link>
        </p>
      </div>
    </div>
  );
}

export default Register;

