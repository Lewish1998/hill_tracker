import { Link } from 'react-router-dom';
import './navbar.css';

const Navbar = () => {
  return (
    <div className="navbar-container">
        <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/hills">Hills</Link></li>
            <li><Link to="/">Random Hill</Link></li>
            <li><Link to="/login">About</Link></li>
            <li><Link to="/signup">Login/Signup</Link></li>
        </ul>
    </div>
  )
}
export default Navbar