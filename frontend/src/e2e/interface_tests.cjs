const { Builder, By } = require("selenium-webdriver")
const firefox = require("selenium-webdriver/firefox")
const assert = require("assert")

var options = new firefox.Options().headless()

;(async function login() {
  let driver = await new Builder()
    .forBrowser("firefox")
    .setFirefoxOptions(options)
    .build()
  try {
    await driver.get("http://localhost:3000/login")
    await driver.findElement(By.id("username")).sendKeys("bruger123")
    await driver.findElement(By.id("password")).sendKeys("123")
    await driver.findElement(By.id("signin")).click()
  } catch (error) {
    console.log(error)
    process.exit(1)
  } finally {
    await driver.quit()
  }
})()
;(async function missingUsernameLogin() {
  let driver = await new Builder()
    .forBrowser("firefox")
    .setFirefoxOptions(options)
    .build()
  try {
    await driver.get("http://localhost:3000/login")
    await driver.findElement(By.id("username")).sendKeys("bruger123")
    assert.equal(false, await driver.findElement(By.id("signin")).isEnabled())
  } catch (error) {
    console.log(error)
    process.exit(1)
  } finally {
    await driver.quit()
  }
})()
;(async function missingPasswordLogin() {
  let driver = await new Builder()
    .forBrowser("firefox")
    .setFirefoxOptions(options)
    .build()
  try {
    await driver.get("http://localhost:3000/login")
    await driver.findElement(By.id("password")).sendKeys("123")
    assert.equal(false, await driver.findElement(By.id("signin")).isEnabled())
  } catch (error) {
    console.log(error)
    process.exit(1)
  } finally {
    await driver.quit()
  }
})()
;(async function incorrectSignInCredentials() {
  let driver = await new Builder()
    .forBrowser("firefox")
    .setFirefoxOptions(options)
    .build()
  try {
    await driver.get("http://localhost:3000/login")
    await driver.findElement(By.id("username")).sendKeys("Egonolsenfan1337")
    await driver.findElement(By.id("password")).sendKeys("pingvin3435")
    await driver.findElement(By.id("signin")).click()
    await driver.manage().setTimeouts({ implicit: 50 })
    assert.equal(
      "Incorrect username or password",
      await driver.findElement(By.id("errorLabel")).getText()
    )
  } catch (error) {
    console.log(error)
    process.exit(1)
  } finally {
    await driver.quit()
  }
})()
