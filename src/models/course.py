#!/usr/bin/env python3

#############################
# Course Model              #
#############################

class Course:
    def __init__(self, course) -> None:
        self.data = course

    @property
    def id(self):
        result = self.data['_id']
        return result

    @property
    def title(self):
        result = f"**🔴 {self.data['title']}**"
        return result

    @property
    def description(self):
        result = None

        if self.data['headline'] and str(self.data['headline']).strip() != '':
            result =f"🎯 {self.data['headline']}"

        return result

    @property
    def image_url(self):
        result = self.data['image_url']
        return result

    @property
    def shorten_url(self):
        result = self.data['shorten_url']
        return result

    @property
    def category(self):
        result = None

        if self.data['category']:
            result = f"🔰 Category: {self.data['category']}"
            
        if self.data['category'] and self.data['subcategory']:
            result += f" / {self.data['subcategory']}"

        if self.data['category'] == None and self.data['subcategory']:
            result = f"🔰 Category: {self.data['subcategory']}"
        
        return result

    @property
    def content_info(self):
        result = f"⏰ Content Info: {self.data['content_info']}"
        return result

    @property
    def instructional_level(self):
        result = f"⏰ Instructional Level: {self.data['instructional_level']}"
        return result

    @property
    def enroll(self):
        url_text = f'https://udemy.com/courses/{self.id}'
        result = f"🔗 Enroll Now: [{url_text}]({self.shorten_url})"
        return result

    @property
    def shared(self):
        result = {self.data['shared']}
        return result

    @property
    def share_text(self):
        result = "🤝 Share and help us grow: @freeudemydiscounts"
        return result

    @property
    def caption(self):
        caption = []

        # Title
        caption.append(self.title)

        # Description
        if self.description:
            caption.append(self.description)

        # Category
        if self.category:
            caption.append(self.category)

        # Content Info
        if self.data['content_info']:
            caption.append(self.content_info)

        # Instructional Level
        if self.data['instructional_level']:
            caption.append(self.instructional_level)

        caption.extend([self.enroll, self.share_text])
        caption = '\n\n'.join(caption)
        return caption