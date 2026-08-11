import { useMemo, useState } from 'react';
import { Plus, Search } from 'lucide-react';
import PageHeader from '../components/PageHeader';
import Modal from '../components/Modal';
import { patients as initialPatients } from '../data/mockData';

const statusStyles = {
  Admitted: 'bg-blue-50 text-blue-700',
  Outpatient: 'bg-slate-100 text-slate-700',
  Critical: 'bg-red-50 text-red-700',
  Stable: 'bg-emerald-50 text-emerald-700',
};

const filters = ['All', 'Admitted', 'Outpatient', 'Critical', 'Stable'];

const emptyForm = { name: '', age: '', gender: 'Male', condition: '', doctor: '', ward: '', status: 'Admitted' };

function nextId(list) {
  const nums = list.map((p) => parseInt(p.id.replace('PT-', ''), 10)).filter((n) => !Number.isNaN(n));
  const max = nums.length ? Math.max(...nums) : 1041;
  return `PT-${max + 1}`;
}

export default function Patients() {
  const [patients, setPatients] = useState(initialPatients);
  const [query, setQuery] = useState('');
  const [filter, setFilter] = useState('All');
  const [showModal, setShowModal] = useState(false);
  const [form, setForm] = useState(emptyForm);
  const [error, setError] = useState('');

  const filtered = useMemo(() => {
    return patients.filter((p) => {
      const matchesFilter = filter === 'All' || p.status === filter;
      const matchesQuery =
        query.trim() === '' ||
        p.name.toLowerCase().includes(query.toLowerCase()) ||
        p.id.toLowerCase().includes(query.toLowerCase());
      return matchesFilter && matchesQuery;
    });
  }, [query, filter, patients]);

  const updateField = (field) => (e) => setForm((prev) => ({ ...prev, [field]: e.target.value }));

  const openModal = () => {
    setForm(emptyForm);
    setError('');
    setShowModal(true);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!form.name.trim() || !form.age.trim() || !form.condition.trim() || !form.doctor.trim() || !form.ward.trim()) {
      setError('Please fill in every field.');
      return;
    }
    const newPatient = { ...form, age: Number(form.age), id: nextId(patients) };
    setPatients((prev) => [newPatient, ...prev]);
    setShowModal(false);
  };

  return (
    <>
      <PageHeader
        eyebrow="Patient records"
        title="Patients"
        subtitle={`${patients.length} patients on file across all wards and OPD`}
      />

      <section className="mt-6 rounded-[28px] border border-slate-200 bg-white p-5 shadow-sm">
        <div className="flex flex-col gap-3 sm:flex-row sm:items-center sm:justify-between">
          <div className="flex items-center gap-2 rounded-2xl border border-slate-200 bg-slate-50 px-4 py-2.5">
            <Search className="h-4 w-4 text-slate-400" />
            <input
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="Search by name or patient ID"
              className="w-56 bg-transparent text-sm outline-none placeholder:text-slate-400"
            />
          </div>
          <div className="flex flex-wrap items-center gap-2">
            {filters.map((f) => (
              <button
                key={f}
                onClick={() => setFilter(f)}
                className={`rounded-full px-4 py-2 text-sm font-medium transition ${
                  filter === f ? 'bg-slate-900 text-white' : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
                }`}
              >
                {f}
              </button>
            ))}
            <button
              onClick={openModal}
              className="ml-1 inline-flex items-center gap-2 rounded-full bg-cyan-600 px-4 py-2 text-sm font-medium text-white hover:bg-cyan-700"
            >
              <Plus className="h-4 w-4" />
              New patient
            </button>
          </div>
        </div>

        <div className="mt-5 overflow-x-auto">
          <table className="w-full min-w-[720px] border-collapse text-left text-sm">
            <thead>
              <tr className="text-xs uppercase tracking-wide text-slate-400">
                <th className="pb-3 pr-4">Patient</th>
                <th className="pb-3 pr-4">Age / Gender</th>
                <th className="pb-3 pr-4">Condition</th>
                <th className="pb-3 pr-4">Doctor</th>
                <th className="pb-3 pr-4">Ward</th>
                <th className="pb-3">Status</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((p) => (
                <tr key={p.id} className="border-t border-slate-100">
                  <td className="py-3 pr-4">
                    <p className="font-medium text-slate-900">{p.name}</p>
                    <p className="text-xs text-slate-400">{p.id}</p>
                  </td>
                  <td className="py-3 pr-4 text-slate-600">{p.age} · {p.gender}</td>
                  <td className="py-3 pr-4 text-slate-600">{p.condition}</td>
                  <td className="py-3 pr-4 text-slate-600">{p.doctor}</td>
                  <td className="py-3 pr-4 text-slate-600">{p.ward}</td>
                  <td className="py-3">
                    <span className={`rounded-full px-3 py-1 text-xs font-medium ${statusStyles[p.status] || 'bg-slate-100 text-slate-700'}`}>
                      {p.status}
                    </span>
                  </td>
                </tr>
              ))}
              {filtered.length === 0 ? (
                <tr>
                  <td colSpan={6} className="py-8 text-center text-slate-400">
                    No patients match your search.
                  </td>
                </tr>
              ) : null}
            </tbody>
          </table>
        </div>
      </section>

      {showModal ? (
        <Modal title="Add new patient" subtitle="Enter the patient's details" onClose={() => setShowModal(false)}>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label className="text-sm font-medium text-slate-700">Full name</label>
              <input
                value={form.name}
                onChange={updateField('name')}
                placeholder="e.g. Rahul Desai"
                className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
              />
            </div>
            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="text-sm font-medium text-slate-700">Age</label>
                <input
                  type="number"
                  min="0"
                  value={form.age}
                  onChange={updateField('age')}
                  className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
                />
              </div>
              <div>
                <label className="text-sm font-medium text-slate-700">Gender</label>
                <select
                  value={form.gender}
                  onChange={updateField('gender')}
                  className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
                >
                  <option>Male</option>
                  <option>Female</option>
                  <option>Other</option>
                </select>
              </div>
            </div>
            <div>
              <label className="text-sm font-medium text-slate-700">Condition</label>
              <input
                value={form.condition}
                onChange={updateField('condition')}
                placeholder="e.g. Routine checkup"
                className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
              />
            </div>
            <div>
              <label className="text-sm font-medium text-slate-700">Doctor</label>
              <input
                value={form.doctor}
                onChange={updateField('doctor')}
                placeholder="e.g. Dr. Rao"
                className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
              />
            </div>
            <div className="grid grid-cols-2 gap-3">
              <div>
                <label className="text-sm font-medium text-slate-700">Ward</label>
                <input
                  value={form.ward}
                  onChange={updateField('ward')}
                  placeholder="e.g. OPD"
                  className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
                />
              </div>
              <div>
                <label className="text-sm font-medium text-slate-700">Status</label>
                <select
                  value={form.status}
                  onChange={updateField('status')}
                  className="mt-1 w-full rounded-xl border border-slate-200 px-3 py-2 text-sm outline-none focus:border-cyan-500"
                >
                  <option>Admitted</option>
                  <option>Outpatient</option>
                  <option>Critical</option>
                  <option>Stable</option>
                </select>
              </div>
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
                Save patient
              </button>
            </div>
          </form>
        </Modal>
      ) : null}
    </>
  );
}