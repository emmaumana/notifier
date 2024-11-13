import { useState } from 'react'
import './index.scss'

enum Topics {
  Sales = 'sales',
  Pricing = 'pricing',
}

const endpoint = '/support-requests'

export const CustomerSupportForm = () => {
  const [receiverEmail, setReceiverEmail] = useState<string>('')
  const [selectedTopic, setSelectedTopic] = useState<Topics | undefined>()
  const [description, setDescription] = useState<string>('')
  const [loading, setLoading] = useState<boolean>(false)
  const formValid = !!receiverEmail && !!selectedTopic && !!description

  const handleSubmit = async () => {
    if (!formValid) return
    setLoading(true)

    const response = await fetch(import.meta.env.VITE_API_BASE_URL + endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        description,
        topic: selectedTopic,
        receiver: receiverEmail,
      }),
    })

    if (response.ok) {
      location.reload()
    } else {
      setLoading(false)
    }
  }

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault(), handleSubmit()
      }}
      className="customer-support-form"
    >
      <div className="form-title">
        <h2>Contact support</h2>
      </div>
      <div className="input-control email">
        <input
          name="email"
          id="email"
          type="email"
          className="input email"
          placeholder="Receiver email..."
          onChange={(event) => setReceiverEmail(event.target.value)}
          value={receiverEmail}
        />
      </div>
      <div className="input-control topic">
        <select
          name="topic"
          id="topic"
          className="topic"
          onChange={(event) => event.target.value && setSelectedTopic(event.target.value as Topics)}
        >
          <option value="" className="topic-option">
            Choose a topic
          </option>
          <option value="sales" className="topic-option">
            Sales
          </option>
          <option value="pricing" className="topic-option">
            Pricing
          </option>
        </select>
      </div>
      <div className="input-control description">
        <textarea
          name="description"
          id="description"
          className="input description"
          placeholder="Describe your issue..."
          onChange={(event) => setDescription(event.target.value)}
          value={description}
        />
      </div>

      <div className="customer-support-form__actions">
        <button type="submit" disabled={!formValid || loading}>
          Send request
        </button>
      </div>
    </form>
  )
}
