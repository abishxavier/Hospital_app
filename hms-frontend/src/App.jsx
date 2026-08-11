import { Route, Routes } from 'react-router-dom';
import DashboardLayout from './components/DashboardLayout';
import Overview from './pages/Overview';
import Patients from './pages/Patients';
import Appointments from './pages/Appointments';
import Doctors from './pages/Doctors';
import Beds from './pages/Beds';
import Billing from './pages/Billing';
import NotFound from './pages/NotFound';

export default function App() {
  return (
    <Routes>
      <Route element={<DashboardLayout />}>
        <Route index element={<Overview />} />
        <Route path="patients" element={<Patients />} />
        <Route path="appointments" element={<Appointments />} />
        <Route path="doctors" element={<Doctors />} />
        <Route path="beds" element={<Beds />} />
        <Route path="billing" element={<Billing />} />
        <Route path="*" element={<NotFound />} />
      </Route>
    </Routes>
  );
}
