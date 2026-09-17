import React, { useEffect } from "react";
import { BrowserRouter, Routes, Route, useLocation } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import NavBar from "./Components/NavBar";
import Footer from "./Components/Footer";
import Home from "./pages/Home";
import Services from "./pages/Services";
import ServiceDetails from "./pages/ServiceDetails";
import Booking from "./pages/Booking";
import BookingSuccess from "./pages/BookingSuccess";
import MyBookings from "./pages/MyBookings";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Button from "./Components/Button";
import "./App.css";

// Scroll to top helper on route change
function ScrollToTop() {
  const { pathname } = useLocation();
  useEffect(() => {
    window.scrollTo(0, 0);
  }, [pathname]);
  return null;
}

// 404 Fallback Component
function NotFound() {
  return (
    <div className="container" style={{ padding: "6rem 1.5rem", textAlign: "center" }}>
      <div style={{ fontSize: "3.5rem", marginBottom: "1rem" }}>🔍</div>
      <h1 style={{ fontSize: "1.8rem", fontWeight: 800, marginBottom: "0.5rem", color: "var(--text-primary)" }}>
        Page Not Found
      </h1>
      <p className="text-muted" style={{ marginBottom: "1.8rem" }}>
        The page you are looking for does not exist or has been moved.
      </p>
      <Button to="/" variant="primary">
        Return to Home
      </Button>
    </div>
  );
}

function App() {
  return (
    <AuthProvider>
      <BrowserRouter>
        <ScrollToTop />
        <div className="app-layout">
          <NavBar />
          <main className="main-content">
            <Routes>
              {/* Home */}
              <Route path="/" element={<Home />} />

              {/* Services Catalog & Details */}
              <Route path="/services" element={<Services />} />
              <Route path="/services/:id" element={<ServiceDetails />} />
              <Route path="/servicesDetails/:id" element={<ServiceDetails />} />

              {/* Booking */}
              <Route path="/book" element={<Booking />} />
              <Route path="/book/:id" element={<Booking />} />
              <Route path="/booking" element={<Booking />} />
              <Route path="/booking/:id" element={<Booking />} />

              {/* Booking Success */}
              <Route path="/booking-success" element={<BookingSuccess />} />
              <Route path="/bookingsuccessfully" element={<BookingSuccess />} />

              {/* My Bookings */}
              <Route path="/my-bookings" element={<MyBookings />} />
              <Route path="/mybooking" element={<MyBookings />} />

              {/* Auth */}
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />

              {/* 404 */}
              <Route path="*" element={<NotFound />} />
            </Routes>
          </main>
          <Footer />
        </div>
      </BrowserRouter>
    </AuthProvider>
  );
}

export default App;
