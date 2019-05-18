def puya(driver, pattern, stop):
    match = False
    option = 'none'
    animeArticle = driver.find_elements_by_css_selector("article")
    for anime in animeArticle:
        title = anime.find_element_by_css_selector("h2")
        download = anime.find_elements_by_css_selector("div[style]")
        for option in download:
            if '720p' in option.text:
                downloadButton = option.find_element_by_css_selector("a:first-child")
        if title.text.startswith(pattern):
                match = True
                downloadUrl = downloadButton.get_attribute('href')
                driver.get(downloadUrl)
                try:
                    resolutionTitle = driver.find_element_by_css_selector("h3:nth-child(1)")
                    torrentButton = driver.find_element_by_css_selector("a.btn.btn-default:nth-child(1)")
                except Exception:
                    driver.refresh()
                    resolutionTitle = driver.find_element_by_css_selector("h3:nth-child(1)")
                    torrentButton = driver.find_element_by_css_selector("a.btn.btn-default:nth-child(1)")
                if '[720p]' in resolutionTitle.text:
                    torrentButton.click()
                    driver.back()
                else:
                    print('Wrong resolution')
                input()
        elif title.text == stop:
            break
    return match