import classes from './footer.module.css';

const Footer = () => {
    return (
        <footer className={classes.footer_section}>
            <div className={classes.container}>
                <div className={classes.footer}>

                    <div className={classes.footer__links}>
                        <ul className={classes.footer__links_ul}>
                            <li className={classes.footer__links_ul_li}>
                                <a href="#" className={classes.footer__links_ul_li_link}>
                                    <img src="/static/img/instagram.svg" alt="" className="footer__links_ul_li-link--img"/>
                                </a>
                            </li>
                            <li className={classes.footer__links_ul_li}>
                                <a href="#" className={classes.footer__links_ul_li_link}>
                                    <img src="/static/img/youtube.svg" alt="" className="footer__links_ul_li-link--img"/>
                                </a>
                            </li>
                            <li className={classes.footer__links_ul_li}>
                                <a href="#" className={classes.footer__links_ul_li_link}>
                                    <img src="/static/img/vk.svg" alt="" className="footer__links_ul_li-link--img"/>
                                </a>
                            </li>
                            <li className={classes.footer__links_ul_li}>
                                <a href="#" className={classes.footer__links_ul_li_link}>
                                    <img src="/static/img/facebook.svg" alt="" className="footer__links_ul_li-link--img"/>
                                </a>
                            </li>
                        </ul>
                    </div>
                    <div className={classes.footer__authors}>
                        <div className={classes.footer__authors_author}>
                            <div className={classes.footer__authors_author, classes.footer__authors_author_makariy}>
                                    Makariy Corp.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
