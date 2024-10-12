import './login.css';
import myImage from './static/GameForgelogo.png';
import GitImage from './static/github-mark.png';
import GoogleImage from './static/google.png';
import { Link } from 'react-router-dom';

function Login() {
    return (
        <div className='main'>
            {/* Dynamic Background Elements */}
            <div className="background-shapes">
                <div className="shape circle"></div>
                <div className="shape square"></div>
                <div className="shape triangle"></div>
            </div>

            <div className="login-main">
                <div className='login-top'>
                    <div className='top-items'>
                        <div className='logo-img'>
                            <img src={myImage} alt='Logo' className='logo' /> 
                            <h3 className='logo-text'>Welcome Back</h3>
                        </div>
                        <div className='logo-info'>
                            <p>Please enter your details to sign in</p>
                        </div>
                    </div>
                    <div className='down-items'> 
                        <div className='Google'>
                            <img src={GoogleImage} alt='google' className='logo-g' />
                            <span>Sign in with Google</span>
                        </div>
                        <div className='Github'>
                            <img src={GitImage} alt='github' className='logo-gh' />
                            <span>Sign in with GitHub</span>
                        </div>
                    </div>
                </div>
                <div className='login-middle'> or</div>
                <div className="login-bottom">
                    <form className="login-forms">
                        <label htmlFor="email">E-Mail Address</label><br />
                        <input 
                            id="email"
                            className='type1' 
                            type='email' 
                            placeholder="Enter your Email" 
                            required 
                        /><br />
                        <label htmlFor="password">Password</label><br />
                        <input 
                            id="password"
                            className='type1' 
                            type='password' 
                            placeholder="Enter Password" 
                            required 
                        /><br />
                        <div className='login-signup'>
                            <div className='left'>
                                <input type='checkbox' id="remember" /> 
                                <label htmlFor="remember">Remember me</label>
                            </div>
                            <div className='right'>
                                <Link to="/forgot-password">Forget Password?</Link>
                            </div>
                        </div>
                        <button type='submit' className='button'>Sign in</button>
                        <p>Don't have an account yet? <Link to="/signup">Sign up</Link></p>
                    </form>
                </div>
            </div>
        </div>
    );
}

export default Login;
