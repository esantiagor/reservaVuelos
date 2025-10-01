import { useState, useEffect } from 'react';
import { getDestinations, createFlight } from '../api/flights';

export default function FlightForm({ user, onCreate }) {
  const [destinations, setDestinations] = useState([]);
  const [destination, setDestination] = useState('');
  const [travelDate, setTravelDate] = useState('');

  useEffect(() => {
    getDestinations().then(res => setDestinations(res.data));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    createFlight({ user: user.id, destination, travel_date: travelDate })
      .then(() => {
        setDestination('');
        setTravelDate('');
        if (onCreate) onCreate(); // Avisamos a App que recargue la lista
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <select value={destination} onChange={e => setDestination(e.target.value)} required>
        <option value="">Destino</option>
        {destinations.map(d => (
          <option key={d.id} value={d.id}>{d.city}</option>
        ))}
      </select>
      <input type="date" value={travelDate} onChange={e => setTravelDate(e.target.value)} required />
      <button type="submit">Reservar vuelo</button>
    </form>
  );
}
