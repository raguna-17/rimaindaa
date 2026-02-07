import axios from "axios";

// 本番バックエンドの URL を直書き
const API_BASE = "https://rimaindaa.onrender.com/api";

console.log("API_BASE:", API_BASE);

const client = axios.create({
    baseURL: API_BASE,
});


export const setToken = (token: string) => {
    client.defaults.headers.common["Authorization"] = `Bearer ${token}`;
};

export default client;
