import React from "react";
import { Link } from "react-router-dom";

const Button = ({
  children,
  variant = "primary",
  size = "md",
  fullWidth = false,
  to,
  onClick,
  type = "button",
  className = "",
  disabled = false,
  ...props
}) => {
  const variantClass = `btn-${variant}`;
  const sizeClass = size === "lg" ? "btn-lg" : size === "sm" ? "btn-sm" : "";
  const fullWidthClass = fullWidth ? "btn-full" : "";
  const combinedClasses = `btn ${variantClass} ${sizeClass} ${fullWidthClass} ${className}`.trim();

  // If `to` is provided, render React Router Link with button styles
  if (to) {
    return (
      <Link to={to} className={combinedClasses} onClick={onClick} {...props}>
        {children}
      </Link>
    );
  }

  return (
    <button
      type={type}
      className={combinedClasses}
      onClick={onClick}
      disabled={disabled}
      {...props}
    >
      {children}
    </button>
  );
};

export default Button;
