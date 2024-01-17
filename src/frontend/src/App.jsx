import "./App.css";
import { Routes, Route, Navigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
// import Layout from "./Layout/Layout";
// import PageNotFound from "./pages/404";
// import Login from "./pages/Login";
// import GeminiProvider from "./context/GeminiContext";

function App() {
  return (
    // <Layout>
    // <GeminiProvider>
    <Routes>
      <Route element={<Navigate to="/products" replace />} />
      <Route index path="/home" element={<HomePage />} />
      {/* <Route path="/login" element={<Login />} /> */}
      {/* <Route path="/*" element={<PageNotFound />} /> */}
    </Routes>
    // </GeminiProvider>
    // </Layout>
  );
}

export default App;
