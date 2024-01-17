import React, { createContext, useContext, useEffect, useState } from "react";
import api from "../services/config";

const GeminiContext = createContext();

function GeminiProvider({ children }) {
  //useState
  const [gemini, setGemini] = useState([]);

  // useEffect
  useEffect(() => {
    const fetchGemini = async () => {
      try {
        setGemini(await api.get("/products"));
      } catch (error) {
        console.log(error.message);
      }
    };
    fetchGemini();
  }, []);
  return (
    <GeminiContext.Provider value={gemini}>{children}</GeminiContext.Provider>
  );
}

const useGemini = () => {
  const gemini = useContext(GeminiContext);
  return gemini;
};

export default GeminiProvider;
export { useGemini };
