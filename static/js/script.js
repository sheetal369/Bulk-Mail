<<<<<<< HEAD
document.querySelector('.bd-navbar').innerHTML = 
`<nav class="navbar navbar-expand-lg">
<div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
        data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03"
        aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 flex-column db-navbar">
            <li class="nav-item">
            <a class="nav-link active"
                href="http://127.0.0.1:5500/Bulk%20Mail/html/index.html">
                <span class="material-symbols-outlined">
add_comment
</span>Compose Mail</a>
            </li>
            <li class="nav-item accordion" id="users">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <p class="accordion-button collapsed" type="button"
                            data-bs-toggle="collapse" data-bs-target="#details-collapsecontact"
                            aria-expanded="false" aria-controls="details-collapseuser" style="line-height: 1.7;">
                            <span class="material-symbols-outlined">contact_emergency</span>Contacts
                        </p>
                    </h2>
                    <div id="details-collapsecontact"
                        class="accordion-collapse details-collapseOne collapse">
                        <div class="accordion-body d-flex flex-column">
                            <a class="nav-link" href="http://127.0.0.1:5500/html/contacts.html">View Contacts</a>
                            <a class="nav-link" href="http://127.0.0.1:5500/html/createcontact.html">Create Contacts</a>
                        </div>
                    </div>
                </div>
            </li>
           
           
       
            
            <li class="nav-item accordion" id="users">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <p class="accordion-button collapsed" type="button"
                            data-bs-toggle="collapse" data-bs-target="#details-collapseregistration"
                            aria-expanded="false" aria-controls="details-collapseuser" style="line-height: 1.7;">
                            <span class="material-symbols-outlined">
                            new_window
                            </span>Groups
                        </p>
                    </h2>
                    <div id="details-collapseregistration"
                        class="accordion-collapse details-collapseOne collapse">
                        <div class="accordion-body d-flex flex-column">
                            <a class="nav-link" href="#">View Groups</a>
                            <a class="nav-link" href="http://127.0.0.1:5500/Bulk%20Mail/html/creategroup.html">Create Group</a>
                        </div>
                    </div>
                </div>
            </li>
        </ul>
    </div>
</div>
</nav>`;
document.querySelector('.db-top-bar').innerHTML =`
<div class="db-lims-logo">
<a href="/">
    <div class="logo">
        <img src="https://i0.wp.com/kantipurinfotech.com/wp-content/uploads/2022/06/aaaaaaa.gif?resize=165%2C57&ssl=1" alt="">
    </div>
</a>
</div>
<div class="db-title">
<h2>E-mail Management System</h2>
</div>
<div class="db-top-bar-right">
<div class="db-user-profile">
    <div class="db-user-profile-right dropdown main">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
            aria-expanded="false">
            <div class="usersmimage-div">
                <img src="https://ui-avatars.com/api/?name=Pradeep+Marasini&rounded=true&background=FB802C&color=ffffff&size=28&bold=true"
                    alt="">
            </div>
            <div>
                <h3 class="username">Pradeep Marasini</h3>
                <p class="userrole">Super Admin</p>
            </div>
        </button>
        <ul class="dropdown-menu ">
            <li><a class="dropdown-item profile" href="">My Account</a></li>
            <li>
                <a class="dropdown-item log-profile" href="">
                    Logout
                </a>
            </li>
        </ul>
    </div>
</div>
=======
document.querySelector('.bd-navbar').innerHTML = 
`<nav class="navbar navbar-expand-lg">
<div class="container-fluid">
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
        data-bs-target="#navbarTogglerDemo03" aria-controls="navbarTogglerDemo03"
        aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarTogglerDemo03">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0 flex-column db-navbar">
            <li class="nav-item">
            <a class="nav-link active"
                href="http://127.0.0.1:5500/Bulk%20Mail/html/index.html">
                <span class="material-symbols-outlined">
add_comment
</span>Compose Mail</a>
            </li>
            <li class="nav-item accordion" id="users">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <p class="accordion-button collapsed" type="button"
                            data-bs-toggle="collapse" data-bs-target="#details-collapsecontact"
                            aria-expanded="false" aria-controls="details-collapseuser" style="line-height: 1.7;">
                            <span class="material-symbols-outlined">contact_emergency</span>Contacts
                        </p>
                    </h2>
                    <div id="details-collapsecontact"
                        class="accordion-collapse details-collapseOne collapse">
                        <div class="accordion-body d-flex flex-column">
                            <a class="nav-link" href="/">View Contacts</a>
                            <a class="nav-link" href="http://127.0.0.1:5500/createcontact.html">Create Contacts</a>
                        </div>
                    </div>
                </div>
            </li>
           
       
            
            <li class="nav-item accordion" id="users">
                <div class="accordion-item">
                    <h2 class="accordion-header">
                        <p class="accordion-button collapsed" type="button"
                            data-bs-toggle="collapse" data-bs-target="#details-collapseregistration"
                            aria-expanded="false" aria-controls="details-collapseuser" style="line-height: 1.7;">
                            <span class="material-symbols-outlined">
                            new_window
                            </span>Groups
                        </p>
                    </h2>
                    <div id="details-collapseregistration"
                        class="accordion-collapse details-collapseOne collapse">
                        <div class="accordion-body d-flex flex-column">
                            <a class="nav-link" href="http://127.0.0.1:5500/Bulk%20Mail/html/groups.html">View Groups</a>
                            <a class="nav-link" href="http://127.0.0.1:5500/Bulk%20Mail/html/creategroup.html">Create Group</a>
                        </div>
                    </div>
                </div>
            </li>
        </ul>
    </div>
</div>
</nav>`;
document.querySelector('.db-top-bar').innerHTML =`
<div class="db-lims-logo">
<a href="/">
    <div class="logo">
        <img src="https://i0.wp.com/kantipurinfotech.com/wp-content/uploads/2022/06/aaaaaaa.gif?resize=165%2C57&ssl=1" alt="">
    </div>
</a>
</div>
<div class="db-title">
<h2>E-mail Management System</h2>
</div>
<div class="db-top-bar-right">
<div class="db-user-profile">
    <div class="db-user-profile-right dropdown main">
        <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown"
            aria-expanded="false">
            <div class="usersmimage-div">
                <img src="https://ui-avatars.com/api/?name=Pradeep+Marasini&rounded=true&background=FB802C&color=ffffff&size=28&bold=true"
                    alt="">
            </div>
            <div>
                <h3 class="username">Pradeep Marasini</h3>
                <p class="userrole">Super Admin</p>
            </div>
        </button>
        <ul class="dropdown-menu ">
            <li><a class="dropdown-item profile" href="">My Account</a></li>
            <li>
                <a class="dropdown-item log-profile" href="">
                    Logout
                </a>
            </li>
        </ul>
    </div>
</div>
>>>>>>> 6a8eeb1dddf10f428144ab36a023a2ec2eb5ec7c
</div>`