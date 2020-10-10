# -*- coding: utf-8 -*-
import python_design_pattern.mvc.model as model


if __name__ == '__main__':
    full_url = 'naver.com'

    url_model = model.Url.shorten(full_url)
    print(url_model.short_url)

    url_model = model.Url.get_By_short_url(url_model.short_url)
    if not url_model:
        raise Exception("not found")

    print(url_model.full_url)
