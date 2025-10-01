import { useEffect, useState } from 'react';
import { getFlights, markReserved } from '../api/flights';
import { Link } from 'react-router-dom';

export default function FlightList({ refresh }) {
  const [flights, setFlights] = useState([]);

  useEffect(() => {
    fetchFlights();
  }, [refresh]);

  const fetchFlights = () => {
    getFlights().then(res => setFlights(res.data));
  };

  const handleReserve = (id) => {
    markReserved(id).then(() => fetchFlights());
  };

  return (
    <div>
      <h2>Lista de vuelos</h2>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Destino</th>
            <th>Fecha</th>
            <th>Estado</th>
            <th>Validar</th>
          </tr>
        </thead>
        <tbody>
          {flights.map(flight => (
            <tr key={flight.id}>
              <td>
                <Link to={`/flights/${flight.id}`}>{flight.id}</Link>
              </td>
              <td>{flight.destination}</td>
              <td>{flight.travel_date}</td>
              <td>{flight.status}</td>
              <td>
                {flight.status !== 'RESERVED' && (
                  <button onClick={() => handleReserve(flight.id)}>
                    Validar
                  </button>
                )}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}