﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using markashleybell.com.Web.Models;
using System.Web.Security;
using markashleybell.com.Web.Abstract;

namespace markashleybell.com.Web.Controllers
{
    public class AccountController : Controller
    {
        IFormsAuthenticationProvider _auth;

        public AccountController(IFormsAuthenticationProvider auth)
        {
            _auth = auth;
        }

        public ActionResult LogOn()
        {
            return View();
        }

        [HttpPost]
        public ActionResult LogOn(LogOnViewModel model, string returnUrl)
        {
            if (ModelState.IsValid)
                if (!_auth.Authenticate(model.Username, model.Password))
                    ModelState.AddModelError("", "Incorrect username or password");

            if (ModelState.IsValid)
            {
                _auth.SetAuthCookie(model.Username, false);
                return Redirect(returnUrl ?? Url.Action("Articles", "Admin"));
            }
            else
            {
                return View();
            }
        }

    }
}