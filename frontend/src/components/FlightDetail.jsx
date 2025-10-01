import { useEffect, useState } from 'react';
import { getFlightDetail } from '../api/flights';

export default function FlightDetail({ flightId }) {
  const [flight, setFlight] = useState(null);

  useEffect(() => {
    getFlightDetail(flightId).then(res => setFlight(res.data));
  }, [flightId]);

  if (!flight) return <p>Cargando...</p>;

  return (
    <div>
      <h2>Detalle de vuelo</h2>
      <p>Usuario: {flight.user}</p>
      <p>Destino: {flight.destination}</p>
      <p>Fecha: {flight.travel_date}</p>
      <p>Estado: {flight.status}</p>
    </div>
  );
}
