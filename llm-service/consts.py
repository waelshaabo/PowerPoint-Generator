PROMPT = """
I want to prepare a short essay about {content}. Assume the role of a professional writer and prepare the text of the essay in a style that can be understood by 15-year-old teens. Ensure that the essay is concise and does not exceed 1000 words.

Then, summarize this essay and convert it into an array of JSON objects suitable for a PowerPoint presentation. 
- Determine the appropriate number of JSON objects (slides) based on the essay's content. 
- Each key point in a slide should be concise, up to 10 words. 
- Include a maximum of 5 bullet points per slide. 
- The JSON should be correctly formatted and valid.

This is a sample of such json object:
 {
 "id": 1,
 "title_text": "My Presentation Title",
 "subtitle_text": "My presentation subtitle",
 "is_title_slide": "yes"
 }
  And here is the sample of json data for slides:
 {"id": 2, title_text": "Slide 1 Title", "text": ["Bullet 1", "Bullet 2"]},
 {"id": 3, title_text": "Slide 2 Title", "text": ["Bullet 1", "Bullet 2", "Bullet 3"]}

Please ensure the JSON array is valid and do not include any explanations or extra text. Return only the JSON array as your output.
"""