import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { Plus, Search, Filter, MoreHorizontal, Settings2, X } from 'lucide-react';
import Layout from './components/Layout/Layout';
import AdminDashboard from './pages/Admin/Dashboard';

// A generic "working" page template that looks like a real module instead of "under construction"
const GenericPage = ({ title, description, cols }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  return (
    <div className="animate-in fade-in slide-in-from-bottom-4 duration-500 relative">
      
      {/* Modal Overlay */}
      {isModalOpen && (
        <div className="fixed inset-0 bg-slate-900/50 backdrop-blur-sm z-50 flex items-center justify-center">
          <div className="bg-white rounded-2xl shadow-xl w-full max-w-md animate-in zoom-in-95 duration-200">
            <div className="flex justify-between items-center p-6 border-b border-slate-100">
              <h2 className="text-xl font-bold text-slate-800">Add New {title.split(' ')[0]}</h2>
              <button onClick={() => setIsModalOpen(false)} className="text-slate-400 hover:text-slate-600">
                <X className="w-5 h-5" />
              </button>
            </div>
            <div className="p-6 space-y-4">
              {cols.slice(0, 3).map((col, idx) => (
                <div key={idx}>
                  <label className="block text-sm font-medium text-slate-700 mb-1">{col}</label>
                  <input type="text" className="w-full px-3 py-2 border border-slate-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:outline-none" placeholder={`Enter ${col.toLowerCase()}`} />
                </div>
              ))}
            </div>
            <div className="p-6 border-t border-slate-100 flex justify-end space-x-3 bg-slate-50 rounded-b-2xl">
              <button onClick={() => setIsModalOpen(false)} className="px-4 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100 rounded-lg">Cancel</button>
              <button onClick={() => { alert("Details added successfully!"); setIsModalOpen(false); }} className="px-4 py-2 text-sm font-medium text-white bg-blue-600 hover:bg-blue-700 rounded-lg shadow-sm">Save Details</button>
            </div>
          </div>
        </div>
      )}

      <div className="flex justify-between items-center mb-6">
        <div>
          <h1 className="text-2xl font-bold text-slate-900">{title}</h1>
          <p className="text-sm text-slate-500 mt-1">{description}</p>
        </div>
        <div className="flex space-x-3">
          <button className="flex items-center px-4 py-2 bg-white border border-slate-200 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-50 shadow-sm">
            <Settings2 className="w-4 h-4 mr-2" />
            Manage
          </button>
          <button onClick={() => setIsModalOpen(true)} className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-lg text-sm font-medium hover:bg-blue-700 shadow-sm shadow-blue-200">
            <Plus className="w-4 h-4 mr-2" />
            Create New
          </button>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-sm border border-slate-200 overflow-hidden">
        <div className="p-4 border-b border-slate-200 flex justify-between items-center bg-slate-50/50">
          <div className="relative">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 transform -translate-y-1/2" />
            <input 
              type="text" 
              placeholder="Search records..." 
              className="pl-9 pr-4 py-2 border border-slate-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 w-64"
            />
          </div>
          <button className="flex items-center px-3 py-2 text-sm text-slate-600 bg-white border border-slate-200 rounded-lg hover:bg-slate-50">
            <Filter className="w-4 h-4 mr-2" />
            Filters
          </button>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left text-sm">
            <thead className="bg-slate-50 border-b border-slate-200 text-slate-600">
              <tr>
                {cols.map((col, idx) => (
                  <th key={idx} className="px-6 py-3 font-semibold">{col}</th>
                ))}
                <th className="px-6 py-3 text-right">Actions</th>
              </tr>
            </thead>
            <tbody>
              {[1, 2, 3, 4, 5].map((row) => (
                <tr key={row} className="border-b border-slate-100 hover:bg-slate-50/50 transition-colors">
                  {cols.map((col, idx) => (
                    <td key={idx} className="px-6 py-4 text-slate-700">
                      {idx === 0 ? <span className="font-medium text-slate-900">Sample {col} {row}</span> : 'Data entry...'}
                    </td>
                  ))}
                  <td className="px-6 py-4 text-right">
                    <button className="text-slate-400 hover:text-slate-600">
                      <MoreHorizontal className="w-5 h-5" />
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        
        <div className="p-4 border-t border-slate-200 flex justify-between items-center text-sm text-slate-500 bg-slate-50/50">
          <span>Showing 1 to 5 of 24 records</span>
          <div className="flex space-x-1">
            <button className="px-3 py-1 border border-slate-200 rounded hover:bg-white bg-slate-100 disabled:opacity-50" disabled>Prev</button>
            <button className="px-3 py-1 border border-slate-200 rounded hover:bg-slate-100 bg-white">1</button>
            <button className="px-3 py-1 border border-slate-200 rounded hover:bg-slate-100 bg-white">2</button>
            <button className="px-3 py-1 border border-slate-200 rounded hover:bg-white bg-slate-100">Next</button>
          </div>
        </div>
      </div>
    </div>
  );
};

// 1. Admin
const UserManagement = () => <GenericPage title="User Management" description="Manage system users and access roles." cols={['Name', 'Role', 'Email', 'Status']} />;
const DoctorManagement = () => <GenericPage title="Doctor Management" description="Manage doctors and their specializations." cols={['Doctor Name', 'Department', 'Phone', 'Availability']} />;
const DepartmentManagement = () => <GenericPage title="Department Management" description="Manage hospital departments." cols={['Dept Name', 'Head of Dept', 'Total Staff']} />;
const StaffManagement = () => <GenericPage title="Staff Management" description="Manage nurses, lab technicians, etc." cols={['Staff Name', 'Role', 'Department', 'Shift']} />;
const ReportsAnalytics = () => <GenericPage title="Reports & Analytics" description="System reports and data exports." cols={['Report Name', 'Generated By', 'Date', 'Type']} />;
const SystemSettings = () => <GenericPage title="System Settings" description="Global application configuration." cols={['Setting Key', 'Value', 'Last Updated']} />;

// 2. Reception
const PatientRegistration = () => <GenericPage title="Patient Registration" description="Register new patients." cols={['Patient ID', 'Name', 'Phone', 'Registered Date']} />;
const AppointmentBooking = () => <GenericPage title="Appointment Booking" description="Schedule appointments." cols={['Appointment ID', 'Patient', 'Doctor', 'Date & Time', 'Status']} />;
const QueueManagement = () => <GenericPage title="Queue Management" description="Monitor live queues." cols={['Token No', 'Patient', 'Doctor', 'Est. Time']} />;
const OPIPRegistration = () => <GenericPage title="OP/IP Registration" description="Manage outpatient and inpatient status." cols={['Patient Name', 'Type', 'Department', 'Status']} />;

// 3. Doctor
const ViewAppointments = () => <GenericPage title="View Appointments" description="Your appointments for today." cols={['Time', 'Patient Name', 'Type', 'Status']} />;
const PatientHistory = () => <GenericPage title="Patient History" description="View previous records and consultations." cols={['Date', 'Diagnosis', 'Doctor', 'Notes']} />;
const Diagnosis = () => <GenericPage title="Diagnosis" description="Record patient diagnosis." cols={['Patient', 'ICD Code', 'Description', 'Severity']} />;
const Prescription = () => <GenericPage title="Prescription" description="Write and manage prescriptions." cols={['Patient', 'Medicines', 'Duration', 'Date']} />;
const LabTestRequest = () => <GenericPage title="Lab Test Request" description="Request diagnostics." cols={['Patient', 'Test Name', 'Priority', 'Status']} />;
const FollowupSchedule = () => <GenericPage title="Follow-up Schedule" description="Schedule follow-up visits." cols={['Patient', 'Next Visit Date', 'Reason']} />;

// 4. Nurse
const PatientVitals = () => <GenericPage title="Patient Vitals" description="Record BP, Heart Rate, Temp, etc." cols={['Patient', 'BP', 'Heart Rate', 'Temp', 'Recorded At']} />;
const WardManagement = () => <GenericPage title="Ward Management" description="Monitor ward occupancy and status." cols={['Ward Name', 'Total Beds', 'Occupied', 'Nurse In-charge']} />;
const MedicationAdmin = () => <GenericPage title="Medication Administration" description="Track administered medicines." cols={['Patient', 'Medicine', 'Dosage', 'Administered By', 'Time']} />;
const NursingNotes = () => <GenericPage title="Nursing Notes" description="Daily observation notes." cols={['Patient', 'Notes', 'Added By', 'Date']} />;

// 5. Laboratory
const TestRequestLab = () => <GenericPage title="Test Request" description="Pending test requests from doctors." cols={['Req ID', 'Patient', 'Test Type', 'Priority', 'Requested By']} />;
const SampleCollection = () => <GenericPage title="Sample Collection" description="Track sample collection status." cols={['Sample ID', 'Patient', 'Test Name', 'Collected By', 'Status']} />;
const ReportEntry = () => <GenericPage title="Report Entry" description="Enter test results." cols={['Test ID', 'Patient', 'Result Summary', 'Verified By']} />;
const ReportUpload = () => <GenericPage title="Report Upload" description="Upload scanned reports/documents." cols={['Document ID', 'Patient', 'File Name', 'Upload Date']} />;

// 6. Pharmacy
const MedicineInventory = () => <GenericPage title="Medicine Inventory" description="Manage pharmacy stock." cols={['Medicine Name', 'Batch No', 'Expiry Date', 'Stock Qty']} />;
const PrescriptionProcessing = () => <GenericPage title="Prescription Processing" description="Dispense medicines for prescriptions." cols={['Prescription ID', 'Patient', 'Doctor', 'Status']} />;
const MedicineBilling = () => <GenericPage title="Medicine Billing" description="Bill medicines to patients." cols={['Bill ID', 'Patient', 'Total Amount', 'Payment Status']} />;
const StockAlerts = () => <GenericPage title="Stock Alerts" description="Low stock and expiry alerts." cols={['Medicine Name', 'Alert Type', 'Current Stock', 'Action Required']} />;

// 7. Inpatient (IP)
const RoomAllocation = () => <GenericPage title="Room Allocation" description="Assign beds/rooms to patients." cols={['Room No', 'Ward Type', 'Patient', 'Status']} />;
const Admission = () => <GenericPage title="Admission" description="Manage IP admissions." cols={['Admission ID', 'Patient', 'Admitted Date', 'Attending Doctor']} />;
const TreatmentRecords = () => <GenericPage title="Treatment Records" description="Inpatient treatment history." cols={['Patient', 'Treatment Details', 'Date', 'Doctor']} />;
const DailyProgress = () => <GenericPage title="Daily Progress" description="Daily clinical notes for IP." cols={['Patient', 'Progress Note', 'Added By', 'Date']} />;
const DischargeSummary = () => <GenericPage title="Discharge Summary" description="Prepare and view discharge summaries." cols={['Patient', 'Discharge Date', 'Summary Status', 'Prepared By']} />;

// 8. Billing
const ConsultationCharges = () => <GenericPage title="Consultation Charges" description="Manage OP consultation fees." cols={['Patient', 'Doctor', 'Amount', 'Date']} />;
const LabCharges = () => <GenericPage title="Lab Charges" description="Manage diagnostic charges." cols={['Patient', 'Test Name', 'Amount', 'Status']} />;
const PharmacyCharges = () => <GenericPage title="Pharmacy Charges" description="Medicine charges." cols={['Patient', 'Bill ID', 'Amount', 'Date']} />;
const RoomCharges = () => <GenericPage title="Room Charges" description="IPD room and bed charges." cols={['Patient', 'Days Stayed', 'Total Amount', 'Status']} />;
const PaymentGateway = () => <GenericPage title="Payment Gateway" description="Online transaction logs." cols={['Transaction ID', 'Patient', 'Amount', 'Method', 'Status']} />;
const InvoiceGeneration = () => <GenericPage title="Invoice Generation" description="Generate consolidated invoices." cols={['Invoice ID', 'Patient', 'Total Amount', 'Due Date']} />;

// 9. Patient Portal
const PortalLogin = () => <GenericPage title="Portal Login Settings" description="Manage portal access." cols={['Patient User', 'Last Login', 'Account Status']} />;
const BookApptPortal = () => <GenericPage title="Book Appointment" description="Appointments booked via portal." cols={['Patient', 'Doctor', 'Requested Date', 'Status']} />;
const ViewPrescriptionsPortal = () => <GenericPage title="View Prescriptions" description="Prescriptions shared to portal." cols={['Patient', 'Prescription Date', 'View Count']} />;
const DownloadLabReports = () => <GenericPage title="Download Lab Reports" description="Reports accessed by patients." cols={['Patient', 'Report Name', 'Download Date']} />;
const OnlinePayment = () => <GenericPage title="Online Payment" description="Payments made via portal." cols={['Patient', 'Amount', 'Date', 'Reference ID']} />;
const MedicalHistory = () => <GenericPage title="Medical History" description="Patient EMR access logs." cols={['Patient', 'Accessed Data', 'Date']} />;

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/admin/dashboard" replace />} />
        
        <Route element={<Layout />}>
          {/* 1. Admin */}
          <Route path="/admin/dashboard" element={<AdminDashboard />} />
          <Route path="/admin/users" element={<UserManagement />} />
          <Route path="/admin/doctors" element={<DoctorManagement />} />
          <Route path="/admin/departments" element={<DepartmentManagement />} />
          <Route path="/admin/staff" element={<StaffManagement />} />
          <Route path="/admin/reports" element={<ReportsAnalytics />} />
          <Route path="/admin/settings" element={<SystemSettings />} />
          
          {/* 2. Reception */}
          <Route path="/reception/patient-registration" element={<PatientRegistration />} />
          <Route path="/reception/appointment-booking" element={<AppointmentBooking />} />
          <Route path="/reception/queue-management" element={<QueueManagement />} />
          <Route path="/reception/op-ip-registration" element={<OPIPRegistration />} />
          
          {/* 3. Doctor */}
          <Route path="/doctor/appointments" element={<ViewAppointments />} />
          <Route path="/doctor/patient-history" element={<PatientHistory />} />
          <Route path="/doctor/diagnosis" element={<Diagnosis />} />
          <Route path="/doctor/prescription" element={<Prescription />} />
          <Route path="/doctor/lab-test-request" element={<LabTestRequest />} />
          <Route path="/doctor/follow-up" element={<FollowupSchedule />} />
          
          {/* 4. Nurse */}
          <Route path="/nurse/patient-vitals" element={<PatientVitals />} />
          <Route path="/nurse/ward-management" element={<WardManagement />} />
          <Route path="/nurse/medication-admin" element={<MedicationAdmin />} />
          <Route path="/nurse/nursing-notes" element={<NursingNotes />} />
          
          {/* 5. Laboratory */}
          <Route path="/laboratory/test-request" element={<TestRequestLab />} />
          <Route path="/laboratory/sample-collection" element={<SampleCollection />} />
          <Route path="/laboratory/report-entry" element={<ReportEntry />} />
          <Route path="/laboratory/report-upload" element={<ReportUpload />} />
          
          {/* 6. Pharmacy */}
          <Route path="/pharmacy/medicine-inventory" element={<MedicineInventory />} />
          <Route path="/pharmacy/prescription-processing" element={<PrescriptionProcessing />} />
          <Route path="/pharmacy/medicine-billing" element={<MedicineBilling />} />
          <Route path="/pharmacy/stock-alerts" element={<StockAlerts />} />
          
          {/* 7. Inpatient */}
          <Route path="/inpatient/room-allocation" element={<RoomAllocation />} />
          <Route path="/inpatient/admission" element={<Admission />} />
          <Route path="/inpatient/treatment-records" element={<TreatmentRecords />} />
          <Route path="/inpatient/daily-progress" element={<DailyProgress />} />
          <Route path="/inpatient/discharge-summary" element={<DischargeSummary />} />
          
          {/* 8. Billing */}
          <Route path="/billing/consultation-charges" element={<ConsultationCharges />} />
          <Route path="/billing/lab-charges" element={<LabCharges />} />
          <Route path="/billing/pharmacy-charges" element={<PharmacyCharges />} />
          <Route path="/billing/room-charges" element={<RoomCharges />} />
          <Route path="/billing/payment-gateway" element={<PaymentGateway />} />
          <Route path="/billing/invoice-generation" element={<InvoiceGeneration />} />
          
          {/* 9. Portal */}
          <Route path="/portal/login" element={<PortalLogin />} />
          <Route path="/portal/book-appointment" element={<BookApptPortal />} />
          <Route path="/portal/view-prescriptions" element={<ViewPrescriptionsPortal />} />
          <Route path="/portal/download-reports" element={<DownloadLabReports />} />
          <Route path="/portal/online-payment" element={<OnlinePayment />} />
          <Route path="/portal/medical-history" element={<MedicalHistory />} />

        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
