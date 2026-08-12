import React from 'react';
import { NavLink } from 'react-router-dom';
import { LayoutDashboard, Users, UserPlus, Stethoscope, Calendar, Building, Settings, ListTodo, Activity, BedDouble, FlaskConical, Pill, Receipt, MonitorSmartphone } from 'lucide-react';

export default function Sidebar() {
  const getNavClass = ({ isActive }) =>
    `flex items-center px-4 py-3 text-sm font-medium rounded-lg mb-1 transition-colors ${
      isActive
        ? 'bg-blue-600 text-white'
        : 'text-slate-600 hover:bg-slate-100 hover:text-slate-900'
    }`;

  return (
    <aside className="w-64 bg-white border-r border-slate-200 h-full flex flex-col">
      <div className="h-16 flex items-center px-6 border-b border-slate-200">
        <h1 className="text-xl font-bold text-blue-600">HealthSync</h1>
      </div>
      
      <nav className="flex-1 overflow-y-auto p-4">
        <div className="mb-6">
          <h2 className="px-4 text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Admin</h2>
          <NavLink to="/admin/dashboard" className={getNavClass}>
            <LayoutDashboard className="w-5 h-5 mr-3" /> Dashboard
          </NavLink>
          <NavLink to="/admin/users" className={getNavClass}>
            <Users className="w-5 h-5 mr-3" /> Staff Management
          </NavLink>
          <NavLink to="/admin/departments" className={getNavClass}>
            <Building className="w-5 h-5 mr-3" /> Departments
          </NavLink>
        </div>

        <div className="mb-6">
          <h2 className="px-4 text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Reception</h2>
          <NavLink to="/reception/registration" className={getNavClass}>
            <UserPlus className="w-5 h-5 mr-3" /> Register Patient
          </NavLink>
          <NavLink to="/reception/appointments" className={getNavClass}>
            <Calendar className="w-5 h-5 mr-3" /> Appointments
          </NavLink>
          <NavLink to="/reception/queue" className={getNavClass}>
            <ListTodo className="w-5 h-5 mr-3" /> Queue Management
          </NavLink>
        </div>

        <div className="mb-6">
          <h2 className="px-4 text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Doctor</h2>
          <NavLink to="/doctor/appointments" className={getNavClass}>
            <Stethoscope className="w-5 h-5 mr-3" /> My Appointments
          </NavLink>
        </div>

        <div className="mb-6">
          <h2 className="px-4 text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Nurse & Ward</h2>
          <NavLink to="/nurse/vitals" className={getNavClass}>
            <Activity className="w-5 h-5 mr-3" /> Patient Vitals
          </NavLink>
          <NavLink to="/inpatient/wards" className={getNavClass}>
            <BedDouble className="w-5 h-5 mr-3" /> Inpatient (IP)
          </NavLink>
        </div>

        <div className="mb-6">
          <h2 className="px-4 text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Diagnostics & Meds</h2>
          <NavLink to="/laboratory/tests" className={getNavClass}>
            <FlaskConical className="w-5 h-5 mr-3" /> Laboratory
          </NavLink>
          <NavLink to="/pharmacy/inventory" className={getNavClass}>
            <Pill className="w-5 h-5 mr-3" /> Pharmacy
          </NavLink>
        </div>

        <div className="mb-6">
          <h2 className="px-4 text-xs font-semibold text-slate-400 uppercase tracking-wider mb-2">Finance & Portal</h2>
          <NavLink to="/billing/invoices" className={getNavClass}>
            <Receipt className="w-5 h-5 mr-3" /> Billing
          </NavLink>
          <NavLink to="/portal/login" className={getNavClass}>
            <MonitorSmartphone className="w-5 h-5 mr-3" /> Patient Portal
          </NavLink>
        </div>
      </nav>
      
      <div className="p-4 border-t border-slate-200">
        <NavLink to="/admin/settings" className={getNavClass}>
            <Settings className="w-5 h-5 mr-3" /> Settings
        </NavLink>
      </div>
    </aside>
  );
}
