import { Button, Checkbox, FormLabel, Input } from "@mui/material"

import './Signup.css';
import { useState } from "react";

const Signup = () => {

    const [firstname, setFirstname] = useState('');
    const [lastname, setLastname] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [emailUpdate, setEmailUpdate] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const formData = {
            firstname: firstname,
            lastname: lastname,
            email: email,
            password: password,
            emailUpdate: emailUpdate
        };

        try {
            const response = await fetch('http://127.0.0.1:5000/users', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            });

            if (response.ok) {
                console.log("User created successfully.")
                setFirstname('')
                setLastname('')
                setEmail('')
                setConfirmPassword('')
                setPassword('')
                setEmailUpdate(false)
            } else {
                console.error("Failed to create user.")
            }
        } catch (error) {
            console.error('Error', error);
        }
    }


  return (
    <div className="signup-container">
        <h1>Sign Up</h1>
        <form className="signup-form" onSubmit={handleSubmit}>
            <FormLabel>First Name: </FormLabel>
            <Input type="text" placeholder="First Name" value={firstname} onChange={e => setFirstname(e.target.value)}required/>
            <FormLabel>Last Name: </FormLabel>
            <Input type="text" placeholder="Last Name" value={lastname} onChange={e => setLastname(e.target.value)} required/>
            <FormLabel>Email: </FormLabel>
            <Input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} required/>
            <FormLabel>Password:</FormLabel>
            <Input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} required/>
            <FormLabel>Confirm Password: </FormLabel>
            <Input type="password" placeholder="Confirm Password" value={confirmPassword} onChange={e => setConfirmPassword(e.target.value)} required/>
            <FormLabel>Subscribe to Email updates: </FormLabel>
            <Checkbox value={emailUpdate} onClick={() => {setEmailUpdate(!emailUpdate)}}/>
            <Button variant="contained" type="submit">Submit</Button>
        </form>
    </div>
  )
}
export default Signup