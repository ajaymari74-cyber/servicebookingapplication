import React, { createContext, useContext, useState, useEffect } from "react";
import { registerUser, loginUser, getApiUrl, setApiUrl } from "../services/mockApi";

const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [currentUser, setCurrentUser] = useState(null);
  const [apiUrl, setApiUrlState] = useState(getApiUrl());

  useEffect(() => {
    try {
      const storedUser = localStorage.getItem("serviq_current_user");
      if (storedUser) {
        const parsed = JSON.parse(storedUser);
        // Normalize name & fullName
        const normalized = {
          ...parsed,
          fullName: parsed.fullName || parsed.name || "",
          name: parsed.fullName || parsed.name || ""
        };
        setCurrentUser(normalized);
      } else {
        // Fallback check legacy serviqUser
        const legacyUser = localStorage.getItem("serviqUser");
        if (legacyUser) {
          const parsed = JSON.parse(legacyUser);
          if (parsed && parsed.email) {
            const normalized = {
              ...parsed,
              fullName: parsed.fullName || parsed.name || parsed.email.split("@")[0],
              name: parsed.fullName || parsed.name || parsed.email.split("@")[0]
            };
            setCurrentUser(normalized);
            localStorage.setItem("serviq_current_user", JSON.stringify(normalized));
          }
        }
      }
    } catch (e) {
      console.error("Failed to parse user session", e);
    }
  }, []);

  const login = async (email, password) => {
    const res = await loginUser(email, password);
    if (res.success && res.user) {
      const normalizedUser = {
        id: res.user.id || Date.now().toString(),
        fullName: res.user.fullName || res.user.name || email.split("@")[0],
        name: res.user.fullName || res.user.name || email.split("@")[0],
        email: res.user.email,
        phone: res.user.phone || "",
        address: res.user.address || "",
        source: res.source || "mockapi"
      };
      setCurrentUser(normalizedUser);
      localStorage.setItem("serviq_current_user", JSON.stringify(normalizedUser));
      return { success: true, user: normalizedUser, source: res.source };
    }
    return { success: false, message: res.message || "Invalid credentials." };
  };

  const register = async (userData) => {
    const res = await registerUser(userData);
    if (res.success && res.user) {
      const normalizedUser = {
        id: res.user.id || Date.now().toString(),
        fullName: res.user.fullName || res.user.name || (userData.email || "").split("@")[0],
        name: res.user.fullName || res.user.name || (userData.email || "").split("@")[0],
        email: res.user.email,
        phone: res.user.phone || "",
        address: res.user.address || "",
        source: res.source || "mockapi"
      };
      setCurrentUser(normalizedUser);
      localStorage.setItem("serviq_current_user", JSON.stringify(normalizedUser));
      return { success: true, user: normalizedUser, source: res.source };
    }
    return { success: false, message: res.message || "Registration failed." };
  };

  const logout = () => {
    setCurrentUser(null);
    localStorage.removeItem("serviq_current_user");
  };

  const updateApiUrl = (newUrl) => {
    setApiUrl(newUrl);
    setApiUrlState(getApiUrl());
  };

  return (
    <AuthContext.Provider value={{ currentUser, login, register, logout, apiUrl, updateApiUrl }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);

