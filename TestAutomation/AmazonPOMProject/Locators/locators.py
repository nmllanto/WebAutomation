class Locators():

    # Login Page object locators
    signin_email_id = "ap_email"
    signin_password_id = "ap_password"
    signin_but_id = "signInSubmit"
    incorrect_pass = "//*[@id='auth-error-message-box']/div/div/ul/li/span"

    # Home Page object locators
    home_username = "//*[@id='nav-link-accountList']/span"
    home_cartlink = "nav-cart"
    home_department ="nav-link-shopall"
    home_logout_id = "nav-item-signout"
    home_account_id = "nav-link-accountList"

    # Electronics Page object locators
    elec_headphone_link_text = "Headphones"

    # Cart Page object locators
    cart_item_count_id = "nav-cart-count"
    proceed_checkout = "//*[@id='sc-buy-box-ptc-button']/span/input"

    # Department menu item objects
    dept_electronic = "//*[@id='nav-flyout-shopAll']/div[2]/a[11]/span"
    boss_soundlink = "//*[@id='search']/div[1]/div[2]/div/span[3]/div[1]/div[2]/div/div/div/div[2]/div[1]/div/div/span/a"
    add_to_cart_id = "add-to-cart-button"
    sidesheet_cart_but = "//*[@id='attach-sidesheet-view-cart-button']/span/input"
