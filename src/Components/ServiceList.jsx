import React, { useState, useMemo } from "react";
import ServiceCard from "./ServiceCard";
import Button from "./Button";
import { servicesData, serviceCategories } from "../data/servicesData";

const ServiceList = ({ defaultCategory = "All", initialSearch = "", limit = null }) => {
  const [selectedCategory, setSelectedCategory] = useState(defaultCategory);
  const [searchQuery, setSearchQuery] = useState(initialSearch);
  const [sortBy, setSortBy] = useState("popular");

  const filteredServices = useMemo(() => {
    let result = servicesData.filter((service) => {
      const matchesCategory =
        selectedCategory === "All" || service.category.toLowerCase() === selectedCategory.toLowerCase();
      const matchesSearch =
        service.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
        service.description.toLowerCase().includes(searchQuery.toLowerCase()) ||
        service.category.toLowerCase().includes(searchQuery.toLowerCase());
      return matchesCategory && matchesSearch;
    });

    if (sortBy === "price-low") {
      result.sort((a, b) => a.price - b.price);
    } else if (sortBy === "price-high") {
      result.sort((a, b) => b.price - a.price);
    } else if (sortBy === "rating") {
      result.sort((a, b) => b.rating - a.rating);
    }

    if (limit) {
      result = result.slice(0, limit);
    }

    return result;
  }, [selectedCategory, searchQuery, sortBy, limit]);

  return (
    <div>
      {/* Category Pills & Filters */}
      <div style={{ marginBottom: "1.8rem" }}>
        {/* Category Pills */}
        <div className="category-pills-row" style={{ justifyContent: "flex-start", marginBottom: "1.2rem" }}>
          {serviceCategories.map((cat) => (
            <button
              key={cat}
              className={`pill-btn ${selectedCategory === cat ? "active" : ""}`}
              onClick={() => setSelectedCategory(cat)}
            >
              {cat}
            </button>
          ))}
        </div>

        {/* Search & Sort Controls */}
        <div style={{ display: "flex", gap: "1rem", flexWrap: "wrap", alignItems: "center", justifyContent: "space-between" }}>
          <div style={{ flex: 1, minWidth: "240px", maxWidth: "420px" }}>
            <div className="hero-search" style={{ margin: 0 }}>
              <span style={{ fontSize: "1rem", marginRight: "0.5rem" }}>🔍</span>
              <input
                type="text"
                placeholder="Search services (e.g. Electrician, AC, Cleaning)..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
              {searchQuery && (
                <button
                  onClick={() => setSearchQuery("")}
                  style={{ background: "none", border: "none", color: "var(--text-muted)", cursor: "pointer", padding: "0 0.4rem" }}
                >
                  ✕
                </button>
              )}
            </div>
          </div>

          <div style={{ display: "flex", alignItems: "center", gap: "0.5rem" }}>
            <span style={{ fontSize: "0.88rem", color: "var(--text-muted)", fontWeight: 600 }}>Sort by:</span>
            <select
              className="form-select"
              style={{ width: "auto", padding: "0.45rem 0.8rem", fontSize: "0.86rem" }}
              value={sortBy}
              onChange={(e) => setSortBy(e.target.value)}
            >
              <option value="popular">Recommended</option>
              <option value="rating">Highest Rated</option>
              <option value="price-low">Price: Low to High</option>
              <option value="price-high">Price: High to Low</option>
            </select>
          </div>
        </div>
      </div>

      {/* Grid of Service Cards */}
      {filteredServices.length > 0 ? (
        <div className="services-grid">
          {filteredServices.map((service) => (
            <ServiceCard key={service.id} service={service} />
          ))}
        </div>
      ) : (
        <div style={{ textAlign: "center", padding: "3.5rem 1.5rem", background: "#ffffff", borderRadius: "var(--radius-md)", border: "1px solid var(--border)" }}>
          <div style={{ fontSize: "2.5rem", marginBottom: "0.75rem" }}>🔍</div>
          <h3 style={{ fontSize: "1.2rem", fontWeight: 700, marginBottom: "0.3rem" }}>No Services Found</h3>
          <p style={{ color: "var(--text-muted)", marginBottom: "1.2rem", fontSize: "0.9rem" }}>
            We couldn't find any service matching "{searchQuery}".
          </p>
          <Button
            variant="secondary"
            onClick={() => {
              setSearchQuery("");
              setSelectedCategory("All");
            }}
          >
            Clear Filters
          </Button>
        </div>
      )}
    </div>
  );
};

export default ServiceList;
