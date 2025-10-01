import axios from 'axios';

const API_URL = '/api/';

export const getDestinations = () => axios.get(`${API_URL}destinations/`);
export const getFlights = () => axios.get(`${API_URL}flights/`);
export const createFlight = (data) => axios.post(`${API_URL}flights/`, data);
export const markReserved = (id) => axios.post(`${API_URL}flights/${id}/mark_reserved/`);
export const getFlightDetail = (id) => axios.get(`${API_URL}flights/${id}/`);
