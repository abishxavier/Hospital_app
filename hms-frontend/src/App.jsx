import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout/Layout';
import AdminDashboard from './pages/Admin/Dashboard';

const PlaceholderPage = ({ title, description, icon: Icon, colorClass, bgClass }) => (
  <div className="animate-in fade-in slide-in-from-bottom-4 duration-700">
    <div className="flex justify-between items-center mb-8">
      <div>
        <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight">{title}</h1>
        <p className="text-slate-500 mt-1">{description}</p>
      </div>
    </div>
    <div className="bg-white rounded-2xl p-12 shadow-sm border border-slate-100 flex flex-col items-center justify-center text-center">
      <div className={`p-6 rounded-3xl ${bgClass} bg-opacity-10 mb-6`}>
        {Icon && <Icon className={`w-16 h-16 ${colorClass}`} />}
      </div>
      <h2 className="text-xl font-bold text-slate-800 mb-2">Module Under Construction</h2>
      <p className="text-slate-500 max-w-md">This module is part of the next development phase. The user interface and backend integrations will be implemented soon.</p>
    </div>
  </div>
);

import { Users, Building, UserPlus, Calendar, ListTodo, Stethoscope, Activity } from 'lucide-react';

const StaffManagement = () => <PlaceholderPage title="Staff Management" description="Manage hospital employees and roles." icon={Users} colorClass="text-blue-600" bgClass="bg-blue-500" />;
const Departments = () => <PlaceholderPage title="Departments" description="Hospital departments configuration." icon={Building} colorClass="text-indigo-600" bgClass="bg-indigo-500" />;

const PatientRegistration = () => <PlaceholderPage title="Patient Registration" description="Register new patients for OP/IP." icon={UserPlus} colorClass="text-emerald-600" bgClass="bg-emerald-500" />;
const Appointments = () => <PlaceholderPage title="Appointment Booking" description="Schedule new patient appointments." icon={Calendar} colorClass="text-rose-600" bgClass="bg-rose-500" />;
const QueueManagement = () => <PlaceholderPage title="Queue Management" description="Manage real-time patient queues." icon={ListTodo} colorClass="text-amber-600" bgClass="bg-amber-500" />;

const DoctorAppointments = () => <PlaceholderPage title="My Appointments" description="Your scheduled patients for today." icon={Stethoscope} colorClass="text-blue-600" bgClass="bg-blue-500" />;
const Consultation = () => <PlaceholderPage title="Consultation Room" description="Diagnosis, Prescription, and Lab requests." icon={Activity} colorClass="text-purple-600" bgClass="bg-purple-500" />;

import { BedDouble, FlaskConical, Pill, Receipt, MonitorSmartphone } from 'lucide-react';

const NurseVitals = () => <PlaceholderPage title="Patient Vitals" description="Record and monitor patient vitals." icon={Activity} colorClass="text-pink-600" bgClass="bg-pink-500" />;
const InpatientWards = () => <PlaceholderPage title="Inpatient & Ward Management" description="Manage rooms, beds, and admissions." icon={BedDouble} colorClass="text-indigo-600" bgClass="bg-indigo-500" />;
const LabTests = () => <PlaceholderPage title="Laboratory" description="Manage test requests and reports." icon={FlaskConical} colorClass="text-cyan-600" bgClass="bg-cyan-500" />;
const PharmacyInventory = () => <PlaceholderPage title="Pharmacy" description="Medicine inventory and prescriptions." icon={Pill} colorClass="text-emerald-600" bgClass="bg-emerald-500" />;
const BillingInvoices = () => <PlaceholderPage title="Billing" description="Patient invoices and payments." icon={Receipt} colorClass="text-amber-600" bgClass="bg-amber-500" />;
const PatientPortal = () => <PlaceholderPage title="Patient Portal" description="Patient login and history view." icon={MonitorSmartphone} colorClass="text-blue-600" bgClass="bg-blue-500" />;

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/admin/dashboard" replace />} />
        
        <Route element={<Layout />}>
          {/* Admin Routes */}
          <Route path="/admin/dashboard" element={<AdminDashboard />} />
          <Route path="/admin/users" element={<StaffManagement />} />
          <Route path="/admin/departments" element={<Departments />} />
          
          {/* Reception Routes */}
          <Route path="/reception/registration" element={<PatientRegistration />} />
          <Route path="/reception/appointments" element={<Appointments />} />
          <Route path="/reception/queue" element={<QueueManagement />} />
          
          {/* Doctor Routes */}
          <Route path="/doctor/appointments" element={<DoctorAppointments />} />
          <Route path="/doctor/consultation/:id" element={<Consultation />} />
          
          {/* Nurse & IP Routes */}
          <Route path="/nurse/vitals" element={<NurseVitals />} />
          <Route path="/inpatient/wards" element={<InpatientWards />} />
          
          {/* Lab & Pharmacy Routes */}
          <Route path="/laboratory/tests" element={<LabTests />} />
          <Route path="/pharmacy/inventory" element={<PharmacyInventory />} />
          
          {/* Billing & Portal Routes */}
          <Route path="/billing/invoices" element={<BillingInvoices />} />
          <Route path="/portal/login" element={<PatientPortal />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
