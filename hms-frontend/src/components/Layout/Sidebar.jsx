import React, { useState, useEffect } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import { 
  ShieldCheck, 
  UserPlus, 
  Stethoscope, 
  HeartPulse, 
  FlaskConical, 
  Pill, 
  BedDouble, 
  Receipt, 
  MonitorSmartphone,
  ChevronDown,
  ChevronRight,
  Circle,
  LogOut
} from 'lucide-react';

const MODULES = [
  {
    id: 'admin',
    title: 'Admin',
    icon: ShieldCheck,
    color: 'text-blue-600',
    submodules: [
      { title: 'Dashboard', path: '/admin/dashboard' },
      { title: 'User Management', path: '/admin/users' },
      { title: 'Doctor Management', path: '/admin/doctors' },
      { title: 'Department Management', path: '/admin/departments' },
      { title: 'Staff Management', path: '/admin/staff' },
      { title: 'Reports & Analytics', path: '/admin/reports' },
      { title: 'System Settings', path: '/admin/settings' },
      { title: 'Deleted Records Log', path: '/admin/deleted-records' },
    ]
  },
  {
    id: 'reception',
    title: 'Reception',
    icon: UserPlus,
    color: 'text-teal-600',
    submodules: [
      { title: 'Patient Registration', path: '/reception/patient-registration' },
      { title: 'Appointment Booking', path: '/reception/appointment-booking' },
      { title: 'Queue Management', path: '/reception/queue-management' },
      { title: 'OP/IP Registration', path: '/reception/op-ip-registration' },
    ]
  },
  {
    id: 'doctor',
    title: 'Doctor',
    icon: Stethoscope,
    color: 'text-green-600',
    submodules: [
      { title: 'View Appointments', path: '/doctor/appointments' },
      { title: 'Patient History', path: '/doctor/patient-history' },
      { title: 'Diagnosis', path: '/doctor/diagnosis' },
      { title: 'Prescription', path: '/doctor/prescription' },
      { title: 'Lab Test Request', path: '/doctor/lab-test-request' },
      { title: 'Follow-up Schedule', path: '/doctor/follow-up' },
    ]
  },
  {
    id: 'nurse',
    title: 'Nurse',
    icon: HeartPulse,
    color: 'text-orange-500',
    submodules: [
      { title: 'Patient Vitals', path: '/nurse/patient-vitals' },
      { title: 'Ward Management', path: '/nurse/ward-management' },
      { title: 'Medication Admin', path: '/nurse/medication-admin' },
      { title: 'Nursing Notes', path: '/nurse/nursing-notes' },
    ]
  },
  {
    id: 'laboratory',
    title: 'Laboratory',
    icon: FlaskConical,
    color: 'text-purple-600',
    submodules: [
      { title: 'Test Request', path: '/laboratory/test-request' },
      { title: 'Sample Collection', path: '/laboratory/sample-collection' },
      { title: 'Report Entry', path: '/laboratory/report-entry' },
      { title: 'Report Upload', path: '/laboratory/report-upload' },
    ]
  },
  {
    id: 'pharmacy',
    title: 'Pharmacy',
    icon: Pill,
    color: 'text-emerald-500',
    submodules: [
      { title: 'Medicine Inventory', path: '/pharmacy/medicine-inventory' },
      { title: 'Prescription Processing', path: '/pharmacy/prescription-processing' },
      { title: 'Medicine Billing', path: '/pharmacy/medicine-billing' },
      { title: 'Stock Alerts', path: '/pharmacy/stock-alerts' },
    ]
  },
  {
    id: 'inpatient',
    title: 'Inpatient (IP)',
    icon: BedDouble,
    color: 'text-rose-500',
    submodules: [
      { title: 'Room Allocation', path: '/inpatient/room-allocation' },
      { title: 'Admission', path: '/inpatient/admission' },
      { title: 'Treatment Records', path: '/inpatient/treatment-records' },
      { title: 'Daily Progress', path: '/inpatient/daily-progress' },
      { title: 'Discharge Summary', path: '/inpatient/discharge-summary' },
    ]
  },
  {
    id: 'billing',
    title: 'Billing',
    icon: Receipt,
    color: 'text-blue-500',
    submodules: [
      { title: 'Consultation Charges', path: '/billing/consultation-charges' },
      { title: 'Lab Charges', path: '/billing/lab-charges' },
      { title: 'Pharmacy Charges', path: '/billing/pharmacy-charges' },
      { title: 'Room Charges', path: '/billing/room-charges' },
      { title: 'Payment Gateway', path: '/billing/payment-gateway' },
      { title: 'Invoice Generation', path: '/billing/invoice-generation' },
    ]
  },
  {
    id: 'portal',
    title: 'Patient Portal',
    icon: MonitorSmartphone,
    color: 'text-indigo-600',
    submodules: [
      { title: 'Login', path: '/portal/login' },
      { title: 'Book Appointment', path: '/portal/book-appointment' },
      { title: 'View Prescriptions', path: '/portal/view-prescriptions' },
      { title: 'Download Lab Reports', path: '/portal/download-reports' },
      { title: 'Online Payment', path: '/portal/online-payment' },
      { title: 'Medical History', path: '/portal/medical-history' },
    ]
  }
];

export default function Sidebar({ isOpenMobile, onCloseMobile, userRole: userRoleProp }) {
  const location = useLocation();
  const activeRole = useMemo(() => {
    if (userRoleProp) return userRoleProp;
    try {
      const savedUserStr = localStorage.getItem('hms_user');
      if (!savedUserStr) return 'admin';
      const parsed = JSON.parse(savedUserStr);
      return parsed?.role || 'admin';
    } catch (e) {
      localStorage.removeItem('hms_user');
      return 'admin';
    }
  }, [userRoleProp]);

  const visibleModules = React.useMemo(() => {
    const r = String(activeRole || '').toLowerCase();
    if (r === 'admin' || r.includes('admin')) return MODULES;
    if (r.includes('doctor')) return MODULES.filter(m => m.id === 'doctor');
    if (r.includes('reception')) {
      return MODULES.filter(m => m.id === 'reception' || m.id === 'billing');
    }
    if (r.includes('lab') || r.includes('laboratory')) {
      return MODULES.filter(m => m.id === 'laboratory');
    }
    if (r.includes('nurse')) return MODULES.filter(m => m.id === 'nurse');
    if (r.includes('pharmacy')) return MODULES.filter(m => m.id === 'pharmacy');
    if (r.includes('inpatient')) return MODULES.filter(m => m.id === 'inpatient');
    if (r.includes('portal')) return MODULES.filter(m => m.id === 'portal');
    return MODULES;
  }, [activeRole]);

  const [openModule, setOpenModule] = useState(() => {
    const currentModule = visibleModules.find(m => location.pathname.startsWith(`/${m.id}`));
    return currentModule ? currentModule.id : (visibleModules[0]?.id || 'admin');
  });

  useEffect(() => {
    const currentModule = visibleModules.find(m => location.pathname.startsWith(`/${m.id}`));
    if (currentModule) {
      setOpenModule(currentModule.id);
    } else if (visibleModules.length > 0 && !visibleModules.some(m => m.id === openModule)) {
      setOpenModule(visibleModules[0].id);
    }
  }, [location.pathname, visibleModules]);

  const toggleModule = (id) => {
    setOpenModule(openModule === id ? null : id);
  };

  return (
    <aside className="w-72 bg-white border-r border-slate-200 h-full flex flex-col shadow-sm">
      <div className="h-16 flex items-center px-6 border-b border-slate-200 shrink-0 justify-between">
        <h1 className="text-xl font-bold text-slate-800 flex items-center">
          <div className="w-8 h-8 bg-blue-600 rounded-lg flex items-center justify-center mr-3 text-white shadow-sm">
            <ShieldCheck className="w-5 h-5" />
          </div>
          HMS Portal
        </h1>
        <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-slate-100 text-slate-600 border border-slate-200">
          {activeRole}
        </span>
      </div>
      
      <nav className="flex-1 overflow-y-auto p-4 space-y-2">
        {visibleModules.map((module) => {
          const isOpen = openModule === module.id;
          const isActive = location.pathname.startsWith(`/${module.id}`);
          const Icon = module.icon;
          
          return (
            <div key={module.id} className="mb-1">
              <button 
                onClick={() => toggleModule(module.id)}
                className={`w-full flex items-center justify-between px-4 py-3 text-sm font-medium rounded-xl transition-colors ${
                  isActive || isOpen

                    ? 'bg-slate-50 text-slate-900 border border-slate-200 shadow-sm' 
                    : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 border border-transparent'
                }`}
              >
                <div className="flex items-center">
                  <Icon className={`w-5 h-5 mr-3 ${module.color}`} />
                  {module.title}
                </div>
                {isOpen ? <ChevronDown className="w-4 h-4 text-slate-400" /> : <ChevronRight className="w-4 h-4 text-slate-400" />}
              </button>
              
              {isOpen && (
                <div className="mt-1 ml-4 pl-4 border-l-2 border-slate-100 py-2 space-y-1">
                  {module.submodules.map((sub) => (
                    <NavLink 
                      key={sub.path}
                      to={sub.path} 
                      className={({ isActive }) => 
                        `flex items-center px-3 py-2 text-sm rounded-lg transition-colors ${
                          isActive 
                            ? 'bg-blue-50 text-blue-700 font-semibold' 
                            : 'text-slate-500 hover:bg-slate-50 hover:text-slate-900'
                        }`
                      }
                    >
                      {({ isActive }) => (
                        <>
                          <Circle className={`w-2 h-2 mr-3 ${isActive ? 'fill-blue-600 text-blue-600' : 'fill-slate-300 text-slate-300'}`} />
                          {sub.title}
                        </>
                      )}
                    </NavLink>
                  ))}
                </div>
              )}
            </div>
          );
        })}
      </nav>

      {/* Footer Switch Account Link */}
      <div className="p-4 border-t border-slate-200 shrink-0 bg-slate-50/50">
        <NavLink
          to="/login"
          className="flex items-center justify-center w-full px-4 py-2.5 bg-white hover:bg-slate-100 text-slate-700 font-bold text-xs rounded-xl border border-slate-200 shadow-sm transition-colors"
        >
          <LogOut className="w-4 h-4 mr-2 text-rose-500" />
          Switch Account / Login
        </NavLink>
      </div>
    </aside>
  );
}
