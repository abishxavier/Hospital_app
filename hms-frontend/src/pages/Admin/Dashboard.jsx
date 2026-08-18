import React, { useState } from 'react';
import { 
  Users, 
  Activity, 
  Calendar, 
  DollarSign, 
  TrendingUp, 
  TrendingDown,
  Clock,
  UserPlus,
  X,
  CheckCircle2,
  FileText,
  Search,
  Filter
} from 'lucide-react';
import { 
  AreaChart, 
  Area, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  ResponsiveContainer,
  Legend
} from 'recharts';

const patientDataThisWeek = [
  { name: 'Mon', patients: 120, opd: 80, ipd: 40 },
  { name: 'Tue', patients: 145, opd: 95, ipd: 50 },
  { name: 'Wed', patients: 130, opd: 85, ipd: 45 },
  { name: 'Thu', patients: 165, opd: 110, ipd: 55 },
  { name: 'Fri', patients: 180, opd: 120, ipd: 60 },
  { name: 'Sat', patients: 90, opd: 60, ipd: 30 },
  { name: 'Sun', patients: 70, opd: 45, ipd: 25 },
];

const patientDataLastWeek = [
  { name: 'Mon', patients: 100, opd: 65, ipd: 35 },
  { name: 'Tue', patients: 115, opd: 75, ipd: 40 },
  { name: 'Wed', patients: 140, opd: 90, ipd: 50 },
  { name: 'Thu', patients: 150, opd: 100, ipd: 50 },
  { name: 'Fri', patients: 160, opd: 105, ipd: 55 },
  { name: 'Sat', patients: 80, opd: 55, ipd: 25 },
  { name: 'Sun', patients: 60, opd: 40, ipd: 20 },
];

const patientDataThisMonth = [
  { name: 'Week 1', patients: 850, opd: 580, ipd: 270 },
  { name: 'Week 2', patients: 920, opd: 630, ipd: 290 },
  { name: 'Week 3', patients: 980, opd: 670, ipd: 310 },
  { name: 'Week 4', patients: 1050, opd: 710, ipd: 340 },
];

const initialActivities = [
  { id: 1, title: 'New patient registered', subtitle: 'John Doe • Cardiology', time: '10 mins ago', category: 'Registration', priority: 'Normal', icon: UserPlus, color: 'text-blue-600', bg: 'bg-blue-100', details: 'Patient John Doe (ID: PAT-1099) registered by Front Desk. Assigned to Dr. Priya Nair for preliminary Cardiology checkup.' },
  { id: 2, title: 'Surgery completed', subtitle: 'Dr. Smith • OT Room 2', time: '45 mins ago', category: 'Surgery', priority: 'High', icon: Activity, color: 'text-emerald-600', bg: 'bg-emerald-100', details: 'Laparoscopic Appendectomy performed successfully in Operation Theatre 2. Patient transferred to Post-Op Recovery Ward.' },
  { id: 3, title: 'Appointment cancelled', subtitle: 'Sarah Connor • Neurology', time: '1 hour ago', category: 'Appointment', priority: 'Medium', icon: Calendar, color: 'text-rose-600', bg: 'bg-rose-100', details: 'Appointment #APT-782 cancelled by patient due to scheduling conflict. Slot reopened for OPD queue.' },
  { id: 4, title: 'Shift Change', subtitle: 'Nursing Staff • ICU Ward', time: '2 hours ago', category: 'Roster', priority: 'Normal', icon: Users, color: 'text-indigo-600', bg: 'bg-indigo-100', details: 'Day Shift nursing staff handed over ICU Bed Occupancy logs to Evening Shift In-charge Nurse Sunita Rao.' },
  { id: 5, title: 'Emergency Bed Allocation', subtitle: 'Patient #402 • ICU Bed 04', time: '3 hours ago', category: 'Emergency', priority: 'Critical', icon: Activity, color: 'text-amber-600', bg: 'bg-amber-100', details: 'Emergency room patient admitted directly to ICU Bed 04. Vitals monitoring initiated.' },
  { id: 6, title: 'Lab Report Verified', subtitle: 'CBC Profile • Aarav Kumar', time: '4 hours ago', category: 'Laboratory', priority: 'Normal', icon: FileText, color: 'text-purple-600', bg: 'bg-purple-100', details: 'Complete Blood Count report verified by Senior Lab Tech Anil Mehta and published to Patient EMR.' },
];

const StatCard = ({ title, value, icon: Icon, trend, trendValue, colorClass, bgClass }) => (
  <div className="bg-white rounded-2xl p-6 shadow-sm border border-slate-100 hover:shadow-md transition-shadow relative overflow-hidden group">
    <div className={`absolute -right-6 -top-6 w-24 h-24 rounded-full opacity-10 transition-transform group-hover:scale-110 ${bgClass}`}></div>
    
    <div className="flex justify-between items-start mb-4 relative z-10">
      <div>
        <p className="text-sm font-medium text-slate-500 mb-1">{title}</p>
        <h3 className="text-3xl font-bold text-slate-800">{value}</h3>
      </div>
      <div className={`p-3 rounded-xl ${bgClass} bg-opacity-10 backdrop-blur-sm`}>
        <Icon className={`w-6 h-6 ${colorClass}`} />
      </div>
    </div>
    
    <div className="flex items-center text-sm relative z-10">
      {trend === 'up' ? (
        <TrendingUp className="w-4 h-4 text-emerald-500 mr-1" />
      ) : (
        <TrendingDown className="w-4 h-4 text-rose-500 mr-1" />
      )}
      <span className={trend === 'up' ? 'text-emerald-500 font-medium' : 'text-rose-500 font-medium'}>
        {trendValue}
      </span>
      <span className="text-slate-400 ml-2">vs last period</span>
    </div>
  </div>
);

export default function AdminDashboard() {
  const [timeframe, setTimeframe] = useState('This Week');
  const [selectedActivity, setSelectedActivity] = useState(null);
  const [showAllActivitiesModal, setShowAllActivitiesModal] = useState(false);
  const [activitySearch, setActivitySearch] = useState('');

  const getChartData = () => {
    if (timeframe === 'Last Week') return patientDataLastWeek;
    if (timeframe === 'This Month') return patientDataThisMonth;
    return patientDataThisWeek;
  };

  const filteredActivities = initialActivities.filter(a => 
    a.title.toLowerCase().includes(activitySearch.toLowerCase()) ||
    a.subtitle.toLowerCase().includes(activitySearch.toLowerCase()) ||
    a.category.toLowerCase().includes(activitySearch.toLowerCase())
  );

  return (
    <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-700 relative">
      
      {/* Activity Details Popup Modal */}
      {selectedActivity && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-md p-6 animate-in zoom-in-95 duration-200">
            <div className="flex justify-between items-start border-b border-slate-100 pb-4 mb-4">
              <div className="flex items-center space-x-3">
                <div className={`p-3 rounded-xl ${selectedActivity.bg}`}>
                  <selectedActivity.icon className={`w-6 h-6 ${selectedActivity.color}`} />
                </div>
                <div>
                  <h3 className="font-bold text-slate-900">{selectedActivity.title}</h3>
                  <p className="text-xs text-slate-500">{selectedActivity.subtitle}</p>
                </div>
              </div>
              <button onClick={() => setSelectedActivity(null)} className="text-slate-400 hover:text-slate-600 p-1">
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="space-y-3 text-sm">
              <div className="flex justify-between py-1.5 border-b border-slate-50">
                <span className="text-slate-500">Timestamp</span>
                <span className="font-semibold text-slate-800 flex items-center">
                  <Clock className="w-3.5 h-3.5 mr-1 text-slate-400" /> {selectedActivity.time}
                </span>
              </div>
              <div className="flex justify-between py-1.5 border-b border-slate-50">
                <span className="text-slate-500">Category</span>
                <span className="font-semibold text-blue-600">{selectedActivity.category}</span>
              </div>
              <div className="flex justify-between py-1.5 border-b border-slate-50">
                <span className="text-slate-500">Priority</span>
                <span className={`font-semibold ${selectedActivity.priority === 'Critical' ? 'text-rose-600' : 'text-emerald-600'}`}>
                  {selectedActivity.priority}
                </span>
              </div>
              <div className="mt-3 bg-slate-50 p-3.5 rounded-xl border border-slate-100">
                <p className="text-xs font-semibold text-slate-500 mb-1">Event Log Description</p>
                <p className="text-xs text-slate-700 leading-relaxed">{selectedActivity.details}</p>
              </div>
            </div>

            <div className="mt-6 flex justify-end">
              <button 
                onClick={() => setSelectedActivity(null)} 
                className="px-5 py-2 text-sm font-semibold text-white bg-blue-600 hover:bg-blue-700 rounded-xl shadow-sm"
              >
                Close Activity Details
              </button>
            </div>
          </div>
        </div>
      )}

      {/* View All Activities Drawer Modal */}
      {showAllActivitiesModal && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-2xl p-6 animate-in zoom-in-95 duration-200">
            <div className="flex justify-between items-center pb-4 border-b border-slate-100 mb-4">
              <div>
                <h2 className="text-xl font-bold text-slate-900">Full Hospital Activity Log</h2>
                <p className="text-xs text-slate-500">Real-time system events, registrations, and medical logs</p>
              </div>
              <button onClick={() => setShowAllActivitiesModal(false)} className="text-slate-400 hover:text-slate-600 p-1">
                <X className="w-5 h-5" />
              </button>
            </div>

            <div className="mb-4 relative">
              <Search className="w-4 h-4 text-slate-400 absolute left-3.5 top-1/2 transform -translate-y-1/2" />
              <input 
                type="text" 
                value={activitySearch} 
                onChange={(e) => setActivitySearch(e.target.value)}
                placeholder="Search activity logs by patient, doctor, or event..." 
                className="pl-10 pr-4 py-2 border border-slate-200 rounded-xl text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
              />
            </div>

            <div className="space-y-3 max-h-96 overflow-y-auto pr-1">
              {filteredActivities.map((act) => {
                const Icon = act.icon;
                return (
                  <div 
                    key={act.id} 
                    onClick={() => setSelectedActivity(act)}
                    className="p-3.5 bg-slate-50 hover:bg-blue-50/50 rounded-xl border border-slate-100 cursor-pointer transition-colors flex justify-between items-center group"
                  >
                    <div className="flex items-center space-x-3">
                      <div className={`p-2.5 rounded-xl ${act.bg}`}>
                        <Icon className={`w-5 h-5 ${act.color}`} />
                      </div>
                      <div>
                        <p className="text-sm font-bold text-slate-800 group-hover:text-blue-600 transition-colors">{act.title}</p>
                        <p className="text-xs text-slate-500 mt-0.5">{act.subtitle}</p>
                      </div>
                    </div>
                    <div className="text-right">
                      <span className="text-xs text-slate-400 block">{act.time}</span>
                      <span className="text-[11px] font-semibold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-full">{act.category}</span>
                    </div>
                  </div>
                );
              })}
            </div>

            <div className="mt-6 flex justify-end">
              <button 
                onClick={() => setShowAllActivitiesModal(false)}
                className="px-5 py-2 text-sm font-semibold text-slate-600 hover:bg-slate-100 rounded-xl"
              >
                Close Log
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Header */}
      <div className="flex justify-between items-center mb-8">
        <div>
          <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight">Hospital Overview</h1>
          <p className="text-slate-500 mt-1">Welcome back, Admin. Here is what's happening today.</p>
        </div>
        <div className="flex space-x-3">
          <button 
            onClick={() => alert("Report downloaded successfully!")}
            className="px-4 py-2 bg-white border border-slate-200 rounded-xl text-sm font-medium text-slate-700 hover:bg-slate-50 transition-colors shadow-sm"
          >
            Export Report
          </button>
          <button 
            onClick={() => setShowAllActivitiesModal(true)}
            className="px-4 py-2 bg-blue-600 text-white rounded-xl text-sm font-medium hover:bg-blue-700 transition-colors shadow-sm shadow-blue-200"
          >
            View Activity Log
          </button>
        </div>
      </div>

      {/* Stats Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-6">
        <StatCard 
          title="Total Patients" 
          value="1,248" 
          icon={Users} 
          trend="up" 
          trendValue="+12%"
          colorClass="text-blue-600"
          bgClass="bg-blue-500"
        />
        <StatCard 
          title="Avg. Occupancy" 
          value="84%" 
          icon={Activity} 
          trend="up" 
          trendValue="+5%"
          colorClass="text-indigo-600"
          bgClass="bg-indigo-500"
        />
        <StatCard 
          title="Appointments" 
          value="342" 
          icon={Calendar} 
          trend="down" 
          trendValue="-2%"
          colorClass="text-rose-600"
          bgClass="bg-rose-500"
        />
        <StatCard 
          title="Total Revenue" 
          value="$45,210" 
          icon={DollarSign} 
          trend="up" 
          trendValue="+18%"
          colorClass="text-emerald-600"
          bgClass="bg-emerald-500"
        />
      </div>

      {/* Charts Section */}
      <div className="grid grid-cols-1 xl:grid-cols-3 gap-6">
        {/* Main Chart */}
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 xl:col-span-2">
          <div className="flex justify-between items-center mb-6">
            <div>
              <h2 className="text-lg font-bold text-slate-800">Patient Flow (OPD vs IPD)</h2>
              <p className="text-xs text-slate-500 mt-0.5">Displaying flow trends for: <span className="font-semibold text-blue-600">{timeframe}</span></p>
            </div>
            <select 
              value={timeframe}
              onChange={(e) => setTimeframe(e.target.value)}
              className="bg-slate-50 border border-slate-200 text-slate-700 text-sm font-semibold rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 block p-2.5 cursor-pointer"
            >
              <option value="This Week">This Week</option>
              <option value="Last Week">Last Week</option>
              <option value="This Month">This Month</option>
            </select>
          </div>
          <div className="h-[300px] w-full">
            <ResponsiveContainer width="100%" height="100%">
              <AreaChart data={getChartData()} margin={{ top: 10, right: 10, left: -20, bottom: 0 }}>
                <defs>
                  <linearGradient id="colorOpd" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#3b82f6" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#3b82f6" stopOpacity={0}/>
                  </linearGradient>
                  <linearGradient id="colorIpd" x1="0" y1="0" x2="0" y2="1">
                    <stop offset="5%" stopColor="#8b5cf6" stopOpacity={0.3}/>
                    <stop offset="95%" stopColor="#8b5cf6" stopOpacity={0}/>
                  </linearGradient>
                </defs>
                <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#e2e8f0" />
                <XAxis dataKey="name" axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 12}} dy={10} />
                <YAxis axisLine={false} tickLine={false} tick={{fill: '#64748b', fontSize: 12}} />
                <Tooltip 
                  contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 6px -1px rgb(0 0 0 / 0.1)' }}
                />
                <Legend verticalAlign="top" height={36}/>
                <Area type="monotone" dataKey="opd" stroke="#3b82f6" strokeWidth={3} fillOpacity={1} fill="url(#colorOpd)" name="Outpatient (OPD)" />
                <Area type="monotone" dataKey="ipd" stroke="#8b5cf6" strokeWidth={3} fillOpacity={1} fill="url(#colorIpd)" name="Inpatient (IPD)" />
              </AreaChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Recent Activity List */}
        <div className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 flex flex-col">
          <div className="flex justify-between items-center mb-4">
            <h2 className="text-lg font-bold text-slate-800">Recent Activity</h2>
            <span className="text-xs font-semibold text-blue-600 bg-blue-50 px-2 py-0.5 rounded-full">Live Log</span>
          </div>
          
          <div className="flex-1 space-y-4 overflow-y-auto pr-1">
            {initialActivities.slice(0, 4).map((act) => {
              const Icon = act.icon;
              return (
                <div 
                  key={act.id} 
                  onClick={() => setSelectedActivity(act)}
                  className="flex items-start p-2.5 hover:bg-slate-50 rounded-xl cursor-pointer transition-colors group"
                >
                  <div className={`${act.bg} p-2 rounded-xl mr-3.5 mt-0.5`}>
                    <Icon className={`w-4 h-4 ${act.color}`} />
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-semibold text-slate-800 group-hover:text-blue-600 transition-colors">{act.title}</p>
                    <p className="text-xs text-slate-500 mt-0.5">{act.subtitle}</p>
                    <p className="text-[11px] text-slate-400 mt-1 flex items-center"><Clock className="w-3 h-3 mr-1"/> {act.time}</p>
                  </div>
                </div>
              );
            })}
          </div>
          
          <button 
            onClick={() => setShowAllActivitiesModal(true)}
            className="mt-4 w-full py-2.5 text-sm font-semibold text-blue-600 bg-blue-50 hover:bg-blue-100 rounded-xl transition-colors"
          >
            View All Activity
          </button>
        </div>
      </div>
    </div>
  );
}
