from dataclasses import dataclass

@dataclass(slots=True, order=True)
class Comment(object):
    pk: int
    post_id: int
    user_name: str
    comment: str
    
    @property
    def get_dict(self):
        return {"pk": self.pk,
                "post_id": self.post_id,
                "user": self.user_name,
                "comment": self.comment}