import { BrowserRouter as Router, Routes, Route, useParams } from 'react-router-dom';
import FlightForm from './components/FlightForm';
import FlightList from './components/FlightList';
import FlightDetail from './components/FlightDetail';
import { useState, useEffect } from 'react';


function FlightDetailWrapper() {
  const { id } = useParams(); // id de la URL
  return <FlightDetail flightId={id} />;
}

export default function App() {
  const user = { id: 1, username: 'testuser' }; // Simulación de usuario conectado
  const [flightsUpdated, setFlightsUpdated] = useState(false);

  // Esto es solo para forzar a FlightList a recargar la lista cuando cambie flightsUpdated
  const handleRefresh = () => {
    setFlightsUpdated(prev => !prev);
  };

  return (
    <Router>
      <div>
        <h1>Reserva de vuelos</h1>
        <Routes>
          {/* Página principal: formulario y lista */}
          <Route path="/" element={
            <>
              <FlightForm user={user} onCreate={handleRefresh}/>
              <FlightList refresh={flightsUpdated} />
            </>
          } />
          {/* Detalle de vuelo */}
          <Route path="/flights/:id" element={<FlightDetailWrapper />} />
        </Routes>
      </div>
    </Router>
  );
}
