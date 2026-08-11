import { useState } from 'react';
import { CalendarPlus, Clock } from 'lucide-react';
import PageHeader from '../components/PageHeader';
import Modal from '../components/Modal';
import { appointments as initialAppointments } from '../data/mockData';

const statusStyles = {
  Confirmed: 'bg-emerald-50 text-emerald-700',
  'In Review': 'bg-amber-50 text-amber-700',
  Waiting: 'bg-slate-100 text-slate-700',
  New: 'bg-cyan-50 text-cyan-700',
};

const emptyForm = { patient: '', doctor: '', department: '', time: '' };

export default function Appointments() {
  const [items, setItems] = useState(initialAppointments);
  const [showModal, setShowModal] = useState(false);
  const [form, setForm] = useState(emptyForm);
  const [error, setError] = useState('');

  const confirm = (time) => {
    setItems((prev) => prev.map((a) => (a.time === time ? { ...a, status: 'Confirmed' } : a)));
  };

  const updateField = (field) => (e) => setForm((prev) => ({ ...prev, [field]: e.target.value }));

  const openModal = () => {
    setForm(emptyForm);
    setError('');
    setShowModal(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!form.patient.trim() || !form.doctor.trim() || !form.department.trim() || !form.time.trim()) {
      setError('Please fill in every field.');
      return;
    }
    if (items.some((a) => a.time === form.time)) {
      setError('That time slot is already booked. Pick a different time.');
      return;
    }
    setItems((prev) =>
      [...prev, { ...form, status: 'New' }].sort((a, b) => a.time.localeCompare(b.time))
    );
    setShowModal(false);
  };

  return (
    <>
      <PageHeader
        eyebrow="Today's schedule"
        title="Appointments"
        subtitle={`${items.length} appointments booked for today across all departments`}
      />

      <section className="mt-6 flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
        <p className="text-sm text-slate-500">Tap "Confirm" to move a waiting appointment into the queue.</p>
        <button
          onClick={openModal}
          className="inline-flex items-center gap-2 rounded-full bg-slate-900 px-4 py-2.5 text-sm font-medium text-white hover:bg-slate-800"
        >
          <CalendarPlus className="h-4 w-4" />
          Book appointment
        </button>
      </section>

      <section className="mt-4 rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm">
        <div className="space-y-3">
          {items.map((item) => (
            <div
              key={item.time}
              className="flex flex-col gap-3 rounded-2xl border border-slate-200 bg-slate-50 px-4 py-3 sm:flex-row sm:items-center sm:justify-between"
            >
              <div className="flex items-center gap-4">
                <div className="flex items-center gap-2 rounded-full bg-cyan-50 px-3 py-1 text-sm font-medium text-cyan-700">
                  <Clock className="h-3.5 w-3.5" />
                  {item.time}
                </div>
                <div>
                  <p className="font-medium text-slate-900">{item.patient}</p>
                  <p className="text-sm text-slate-500">{item.doctor} · {item.department}</p>
                </div>
              </div>
              <div className="flex items-center gap-3">
                <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusStyles[item.status] || 'bg-slate-100 text-slate-700'}`}>
                  {item.status}
                </span>
                {item.status !== 'Confirmed' ? (
                  <button
                    onClick={() => confirm(item.time)}
                    className="rounded-full bg-slate-900 px-3 py-1.5 text-xs font-medium text-white"
                  >
                    Confirm
                  </button>
                ) : null}
              </div>
            </div>
          ))}
        </div>
      </section>

      {showModal ? (
        <Modal title="Book appointment" subtitle="Enter the details for the new appointment" onClose={() => setShowModal(false)}>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="text-sm font-medium text-slate-700">Patient name</label>
              <input
                value={form.patient}
                onChange={updateField('patient')}
                placeholder="e.g. Priya Menon"
                className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
              />
            </div>
            <div>
              <label className="text-sm font-medium text-slate-700">Doctor</label>
              <input
                value={form.doctor}
                onChange={updateField('doctor')}
                placeholder="e.g. Dr. Nair"
                className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
              />
            </div>
            <div>
              <label className="text-sm font-medium text-slate-700">Department</label>
              <input
                value={form.department}
                onChange={updateField('department')}
                placeholder="e.g. Cardiology"
                className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
              />
            </div>
            <div>
              <label className="text-sm font-medium text-slate-700">Time</label>
              <input
                type="time"
                value={form.time}
                onChange={updateField('time')}
                className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
              />
            </div>

            {error ? <p className="text-sm text-red-600">{error}</p> : null}

            <div className="flex justify-end gap-2 pt-2">
              <button
                type="button"
                onClick={() => setShowModal(false)}
                className="rounded-full px-4 py-2 text-sm font-medium text-slate-600 hover:bg-slate-100"
              >
                Cancel
              </button>
              <button type="submit" className="rounded-full bg-cyan-600 px-4 py-2 text-sm font-medium text-white hover:bg-cyan-700">
                Save appointment
              </button>
            </div>
          </form>
        </Modal>
      ) : null}
    </>
  );
}