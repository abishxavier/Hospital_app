import React, { useState } from 'react';
import { Bell, UserCircle, X, CheckCircle2, Shield, LogOut, Menu } from 'lucide-react';

export default function Header({ onToggleMobileMenu, user: userProp, onLogout }) {
  const [showNotifications, setShowNotifications] = useState(false);
  const [showLogoutModal, setShowLogoutModal] = useState(false);
  const [showProfileModal, setShowProfileModal] = useState(false);

  const user = userProp || (() => {
    try {
      const savedUserStr = localStorage.getItem('hms_user');
      if (!savedUserStr) return null;
      const parsed = JSON.parse(savedUserStr);
      return parsed && typeof parsed === 'object' ? parsed : null;
    } catch (e) {
      localStorage.removeItem('hms_user');
      return null;
    }
  })() || { name: 'Dr. Sarah Johnson', role: 'admin', email: 'admin@hospital.com' };

  const roleTitleMap = {
    admin: 'Chief Administrator',
    doctor: 'Medical Specialist',
    receptionist: 'Hospital Receptionist',
    reception: 'Hospital Receptionist',
    laboratory: 'Lab Technician',
    lab: 'Lab Technician',
    nurse: 'Staff Nurse',
    pharmacy: 'Pharmacist',
    inpatient: 'IPD Ward Manager'
  };

  const currentRoleTitle = roleTitleMap[String(user?.role).toLowerCase()] || user?.role || 'Staff User';

  const [liveNotifs, setLiveNotifs] = useState([]);

  React.useEffect(() => {
    if (user?.role === 'doctor' && user?.name) {
      fetch(`/api/v1/doctor/notifications?doctor_name=${encodeURIComponent(user.name)}`)
        .then((res) => res.ok ? res.json() : [])
        .then((data) => {
          if (Array.isArray(data) && data.length > 0) {
            setLiveNotifs(data.map((n, idx) => ({
              id: n.id || idx + 1,
              title: 'New Patient Assignment',
              time: 'Just now',
              type: 'urgent',
              text: n.Message || `🔔 New Patient Assigned: ${n.Patient} registered by Receptionist.`
            })));
          }
        })
        .catch(() => {});
    }
  }, [user]);

  const defaultNotifications = [
    { id: 101, title: 'Emergency Room Alert', time: '5m ago', type: 'urgent', text: 'Bed allocation needed for Patient #402 in ICU.' },
    { id: 102, title: 'Lab Results Ready', time: '18m ago', type: 'info', text: 'CBC Blood test report generated for Aarav Kumar.' }
  ];

  const notifications = liveNotifs.length > 0 ? liveNotifs : defaultNotifications;

  const handleConfirmLogout = () => {
    setShowLogoutModal(false);
    if (onLogout) {
      onLogout();
    } else {
      localStorage.removeItem('hms_user');
      window.location.href = '/login';
    }
  };

  return (
    <>
      <header className="h-16 bg-white border-b border-slate-200 flex items-center justify-between px-6 relative z-30">
        <div className="flex items-center space-x-3">
          <button 
            onClick={onToggleMobileMenu} 
            className="md:hidden text-slate-500 hover:text-slate-700 p-1 rounded-lg hover:bg-slate-100"
          >
            <Menu className="w-6 h-6" />
          </button>
          <span className="text-xs font-semibold uppercase tracking-wider text-slate-400 bg-slate-100 px-2.5 py-1 rounded-md">
            Hospital System v1.0
          </span>
        </div>
        
        <div className="flex items-center space-x-4">
          {/* Notification Button */}
          <div className="relative">
            <button 
              onClick={() => setShowNotifications(!showNotifications)}
              className="text-slate-500 hover:text-slate-700 p-2 rounded-xl hover:bg-slate-100 transition-colors relative"
            >
              <Bell className="w-5 h-5" />
              <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-rose-500 rounded-full ring-2 ring-white"></span>
            </button>

            {/* Notification Popover */}
            {showNotifications && (
              <div className="absolute right-0 mt-2 w-80 sm:w-96 bg-white rounded-2xl shadow-xl border border-slate-100 p-4 animate-in fade-in zoom-in-95 duration-200 z-50">
                <div className="flex justify-between items-center pb-3 border-b border-slate-100 mb-3">
                  <div className="flex items-center space-x-2">
                    <h3 className="font-bold text-slate-800 text-sm">Notifications</h3>
                    <span className="bg-blue-100 text-blue-700 text-xs px-2 py-0.5 rounded-full font-semibold">3 New</span>
                  </div>
                  <button onClick={() => setShowNotifications(false)} className="text-slate-400 hover:text-slate-600">
                    <X className="w-4 h-4" />
                  </button>
                </div>
                <div className="space-y-2 max-h-72 overflow-y-auto">
                  {notifications.map((item) => (
                    <div key={item.id} className="p-3 bg-slate-50 rounded-xl hover:bg-slate-100 transition-colors">
                      <div className="flex justify-between items-start mb-1">
                        <span className={`text-xs font-semibold ${item.type === 'urgent' ? 'text-rose-600' : 'text-blue-600'}`}>
                          {item.title}
                        </span>
                        <span className="text-[10px] text-slate-400">{item.time}</span>
                      </div>
                      <p className="text-xs text-slate-600">{item.text}</p>
                    </div>
                  ))}
                </div>
                <button 
                  onClick={() => setShowNotifications(false)} 
                  className="mt-3 w-full py-2 text-center text-xs font-semibold text-blue-600 hover:bg-blue-50 rounded-lg transition-colors"
                >
                  Mark all as read
                </button>
              </div>
            )}
          </div>
          
          {/* User Profile Trigger */}
          <div 
            onClick={() => setShowProfileModal(!showProfileModal)}
            className="flex items-center space-x-3 border-l pl-4 border-slate-200 cursor-pointer hover:opacity-80 transition-opacity"
          >
            <div className="relative">
              <UserCircle className="w-9 h-9 text-slate-600" />
              <span className="absolute bottom-0 right-0 w-2.5 h-2.5 bg-emerald-500 border-2 border-white rounded-full"></span>
            </div>
            <div className="text-sm hidden sm:block">
              <p className="font-semibold text-slate-900 leading-tight">{user?.name || 'Dr. Sarah Johnson'}</p>
              <p className="text-slate-500 text-xs">{currentRoleTitle}</p>
            </div>
          </div>

          {/* Logout Button */}
          <button 
            onClick={() => setShowLogoutModal(true)}
            className="ml-2 px-3 py-1.5 text-sm font-medium text-rose-600 bg-rose-50 hover:bg-rose-100 rounded-lg transition-colors border border-rose-200 flex items-center"
          >
            <LogOut className="w-4 h-4 mr-1.5" />
            <span className="hidden sm:inline">Log Out</span>
          </button>
        </div>
      </header>

      {/* Logout Modal */}
      {showLogoutModal && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-sm p-6 text-center animate-in zoom-in-95 duration-200">
            <div className="w-12 h-12 bg-rose-100 text-rose-600 rounded-full flex items-center justify-center mx-auto mb-4">
              <LogOut className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-slate-900 mb-2">Confirm Logout</h3>
            <p className="text-sm text-slate-500 mb-6">Are you sure you want to end your current session?</p>
            <div className="flex space-x-3 justify-center">
              <button 
                onClick={() => setShowLogoutModal(false)}
                className="px-4 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 rounded-xl flex-1"
              >
                Cancel
              </button>
              <button 
                onClick={handleConfirmLogout}
                className="px-4 py-2 text-sm font-medium text-white bg-rose-600 hover:bg-rose-700 rounded-xl shadow-sm flex-1"
              >
                Log Out
              </button>
            </div>
          </div>
        </div>
      )}


      {/* Profile Details Modal */}
      {showProfileModal && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-md p-6 animate-in zoom-in-95 duration-200">
            <div className="flex justify-between items-center border-b border-slate-100 pb-4 mb-4">
              <div className="flex items-center space-x-3">
                <div className="w-10 h-10 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center font-bold">
                  SJ
                </div>
                <div>
                  <h3 className="font-bold text-slate-900">Dr. Sarah Johnson</h3>
                  <p className="text-xs text-slate-500">sarah.johnson@hospital.org</p>
                </div>
              </div>
              <button onClick={() => setShowProfileModal(false)} className="text-slate-400 hover:text-slate-600">
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <div className="space-y-3 text-sm">
              <div className="flex justify-between py-2 border-b border-slate-50">
                <span className="text-slate-500">Role</span>
                <span className="font-semibold text-slate-800">Administrator / Cardiology Head</span>
              </div>
              <div className="flex justify-between py-2 border-b border-slate-50">
                <span className="text-slate-500">Department</span>
                <span className="font-semibold text-slate-800">Cardiology</span>
              </div>
              <div className="flex justify-between py-2 border-b border-slate-50">
                <span className="text-slate-500">Access Privileges</span>
                <span className="font-semibold text-emerald-600 flex items-center">
                  <Shield className="w-4 h-4 mr-1" /> Full Superadmin
                </span>
              </div>
              <div className="flex justify-between py-2">
                <span className="text-slate-500">Status</span>
                <span className="font-semibold text-emerald-600 flex items-center">
                  <CheckCircle2 className="w-4 h-4 mr-1" /> Active
                </span>
              </div>
            </div>

            <div className="mt-6 flex justify-end">
              <button 
                onClick={() => setShowProfileModal(false)} 
                className="px-4 py-2 text-sm font-semibold text-white bg-blue-600 hover:bg-blue-700 rounded-xl"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
}
