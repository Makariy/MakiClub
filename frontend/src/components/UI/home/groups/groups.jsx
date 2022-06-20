import { useState, useEffect } from 'react';
import { fetchGroups } from '../../../../API/fetcher';
import Group from './group/group';

import classes from './groups.module.css';



const Groups = () => {

    const [groups, setGroups] = useState(null);

    useEffect(() => {
        fetchGroups().then(data => setGroups(data.groups));
    }, []);

    return (
        <section className={classes.groups_section}>
            <div className={classes.container}>
                <div className={classes.groups}>
                    {
                        !groups ? "" : 
                            groups.map(group => <Group {...group} key={group.group.uuid}/>) 
                    }
                </div>
            </div>
        </section>
    );
}

export default Groups;
