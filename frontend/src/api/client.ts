import axios from "axios";

const API_BASE = import.meta.env.VITE_API_URL || "https://rimaindaa-1.onrender.com";

const client = axios.create({
    baseURL: API_BASE,
});

export const setToken = (token: string) => {
    client.defaults.headers.common["Authorization"] = `Bearer ${token}`;
};

export default client;
