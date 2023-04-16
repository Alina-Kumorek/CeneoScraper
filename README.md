# CeneoScraper
| **Składowa** | **Nazwa** | **Selektor** |
| --- | --- | --- |
| Opinia | opinion / single opinion | div.js\_product-review |
| Identyfikator opinii | opinion\_id | [data-entry-id] |
| Autor | author | span.user-post\_\_author-name |
| Rekomendacja | recommendation | span.user-post\_\_author-recomendation \> em |
| Liczba gwiazdek | score | span.user-post\_\_score-count |
| Czy opinia jest potwierdzona zakupem? | purchased | div.review-pz |
| Data wystawienia opinii | opinion\_date | span.user-post\_\_published \> time:nth-child(1)[datetime] |
| Data zakupu produktu | purchase\_date | span.user-post\_\_published \> time:nth-child(2)[datetime] |
| Ile osób uznało opinię za przydatną? | likes | button.vote-yes \> spanbutton.vote-yes[data-total-vote] |
| Ile osób uznało opinię za nieprzydatną? | dislikes | button.vote-no \> spanbutton.vote-no[data-total-vote] |
| Treść opinii | content | div.user-post\_\_text |
| Lista wad | cons | div.review-feature\_\_title--positives ~ div.review-feature\_\_item |
| Lista zalet | pros | div.review-feature\_\_title--negatives ~ div.review-feature\_\_item |