import React from "react";
import { useSearchParams } from "react-router-dom";
import ServiceList from "../Components/ServiceList";

export const Services = () => {
  const [searchParams] = useSearchParams();
  const initialCategory = searchParams.get("cat") || "All";
  const initialQuery = searchParams.get("q") || "";

  return (
    <div style={{ padding: "2.5rem 0 4.5rem" }}>
      <div className="container">
        <div style={{ marginBottom: "1.8rem" }}>
          <h1 className="page-title">All Services</h1>
          <p className="page-subtitle">
            Select a service below to view details or book an appointment.
          </p>
        </div>

        <ServiceList
          defaultCategory={initialCategory}
          initialSearch={initialQuery}
        />
      </div>
    </div>
  );
};

export default Services;
