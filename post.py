import json


class Post:

    def __init__(self, poster_name, poster_avatar, pic, content, views_count, likes_count, pk, tags):
        self.poster_name = poster_name
        self.poster_avatar = poster_avatar
        self.pic = pic
        self.content = content
        self.views_count = views_count
        self.likes_count = likes_count
        self.pk = pk
        self.content_length = len(self.content)
        self.tags = tags
        self.bookmark = False

    def __repr__(self):
        return f"{self.poster_name}, {self.poster_avatar}, {self.pic}, {self.content}, {self.views_count}, {self.likes_count}, {self.pk}, {self.tags}"

    def to_json(self):
        """Вывод для API"""
        return json.dumps({
            "poster_name": self.poster_name,
            "poster_avatar": self.poster_avatar,
            "pic": self.pic,
            "content": self.content,
            "views_count": self.views_count,
            "likes_count": self.likes_count,
            "pk": self.pk,
            "tags": self.tags
        }, ensure_ascii=False)

    def __str__(self) -> str:
        """Обёртка для метода to_json, чтобы был правильный вывод"""
        return self.to_json()
