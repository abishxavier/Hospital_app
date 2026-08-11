export const metrics = [
  { label: 'Admissions', value: '1,248', detail: '+12% vs last month', tint: 'from-cyan-500 to-blue-600' },
  { label: 'ICU Occupancy', value: '82%', detail: '3 critical beds active', tint: 'from-fuchsia-500 to-violet-600' },
  { label: 'Revenue', value: '₹18.4L', detail: 'Collected this week', tint: 'from-emerald-500 to-teal-600' },
  { label: 'Avg. Wait Time', value: '14 min', detail: 'Improved by 6 mins', tint: 'from-amber-500 to-orange-600' },
];

export const flowData = [
  { name: 'Mon', patients: 54, revenue: 130 },
  { name: 'Tue', patients: 66, revenue: 155 },
  { name: 'Wed', patients: 58, revenue: 148 },
  { name: 'Thu', patients: 74, revenue: 182 },
  { name: 'Fri', patients: 71, revenue: 168 },
  { name: 'Sat', patients: 89, revenue: 220 },
];

export const serviceMix = [
  { name: 'OPD', value: 40, color: '#2563eb' },
  { name: 'IPD', value: 28, color: '#14b8a6' },
  { name: 'Lab', value: 20, color: '#f59e0b' },
  { name: 'Pharma', value: 12, color: '#8b5cf6' },
];

export const patients = [
  { id: 'PT-1042', name: 'Aarav Kumar', age: 34, gender: 'Male', condition: 'Post-op recovery', doctor: 'Dr. Nair', ward: 'General - B12', status: 'Admitted' },
  { id: 'PT-1043', name: 'Meera Shah', age: 28, gender: 'Female', condition: 'Routine checkup', doctor: 'Dr. Rao', ward: 'OPD', status: 'Outpatient' },
  { id: 'PT-1044', name: 'Ravi Joshi', age: 61, gender: 'Male', condition: 'Cardiac observation', doctor: 'Dr. Sinha', ward: 'ICU - 3', status: 'Critical' },
  { id: 'PT-1045', name: 'Ananya Verma', age: 45, gender: 'Female', condition: 'Fracture management', doctor: 'Dr. Kapoor', ward: 'Ortho - A4', status: 'Admitted' },
  { id: 'PT-1046', name: 'Karthik Iyer', age: 19, gender: 'Male', condition: 'Fever, dehydration', doctor: 'Dr. Nair', ward: 'General - B07', status: 'Stable' },
  { id: 'PT-1047', name: 'Priya Menon', age: 52, gender: 'Female', condition: 'Diabetes management', doctor: 'Dr. Rao', ward: 'OPD', status: 'Outpatient' },
  { id: 'PT-1048', name: 'Suresh Pillai', age: 70, gender: 'Male', condition: 'Respiratory support', doctor: 'Dr. Sinha', ward: 'ICU - 1', status: 'Critical' },
  { id: 'PT-1049', name: 'Divya Nambiar', age: 8, gender: 'Female', condition: 'Pediatric observation', doctor: 'Dr. Kapoor', ward: 'Pediatrics - P2', status: 'Stable' },
];

export const appointments = [
  { time: '09:30', patient: 'Aarav Kumar', doctor: 'Dr. Nair', department: 'Cardiology', status: 'Confirmed' },
  { time: '10:15', patient: 'Nikhil Rao', doctor: 'Dr. Kapoor', department: 'Orthopedics', status: 'Confirmed' },
  { time: '11:00', patient: 'Meera Shah', doctor: 'Dr. Rao', department: 'General Medicine', status: 'In Review' },
  { time: '11:45', patient: 'Farah Sheikh', doctor: 'Dr. Bhatt', department: 'Dermatology', status: 'Waiting' },
  { time: '01:15', patient: 'Ravi Joshi', doctor: 'Dr. Sinha', department: 'Cardiology', status: 'New' },
  { time: '02:30', patient: 'Sanya Kapoor', doctor: 'Dr. Nair', department: 'Pediatrics', status: 'Confirmed' },
  { time: '03:00', patient: 'Devansh Gupta', doctor: 'Dr. Rao', department: 'General Medicine', status: 'Waiting' },
];

export const doctors = [
  { name: 'Dr. Anjali Nair', specialty: 'Cardiology', patientsToday: 12, status: 'Available', experience: '14 yrs' },
  { name: 'Dr. Kiran Rao', specialty: 'General Medicine', patientsToday: 18, status: 'In Consult', experience: '9 yrs' },
  { name: 'Dr. Devika Sinha', specialty: 'Cardiology (ICU)', patientsToday: 6, status: 'On Rounds', experience: '20 yrs' },
  { name: 'Dr. Arjun Kapoor', specialty: 'Orthopedics', patientsToday: 9, status: 'Available', experience: '11 yrs' },
  { name: 'Dr. Farah Bhatt', specialty: 'Dermatology', patientsToday: 15, status: 'In Consult', experience: '7 yrs' },
  { name: 'Dr. Rohan Mehta', specialty: 'Pediatrics', patientsToday: 10, status: 'Off Duty', experience: '13 yrs' },
];

export const wards = [
  { name: 'General Ward A', total: 30, occupied: 22 },
  { name: 'General Ward B', total: 30, occupied: 26 },
  { name: 'ICU', total: 12, occupied: 10 },
  { name: 'Pediatrics', total: 16, occupied: 7 },
  { name: 'Orthopedics', total: 18, occupied: 12 },
  { name: 'Maternity', total: 14, occupied: 9 },
];

export const invoices = [
  { id: 'INV-3021', patient: 'Aarav Kumar', service: 'Surgery + 3 day stay', amount: 84500, status: 'Paid', date: '05 Aug 2026' },
  { id: 'INV-3022', patient: 'Ravi Joshi', service: 'ICU observation', amount: 132000, status: 'Pending', date: '07 Aug 2026' },
  { id: 'INV-3023', patient: 'Meera Shah', service: 'OPD consultation', amount: 1200, status: 'Paid', date: '08 Aug 2026' },
  { id: 'INV-3024', patient: 'Ananya Verma', service: 'Fracture cast + X-ray', amount: 15600, status: 'Paid', date: '08 Aug 2026' },
  { id: 'INV-3025', patient: 'Suresh Pillai', service: 'ICU + ventilator', amount: 210000, status: 'Overdue', date: '02 Aug 2026' },
  { id: 'INV-3026', patient: 'Divya Nambiar', service: 'Pediatric checkup', amount: 900, status: 'Paid', date: '09 Aug 2026' },
];

export const revenueByDept = [
  { name: 'Cardiology', value: 420000 },
  { name: 'Orthopedics', value: 265000 },
  { name: 'General Medicine', value: 180000 },
  { name: 'Pediatrics', value: 96000 },
  { name: 'Dermatology', value: 62000 },
];
