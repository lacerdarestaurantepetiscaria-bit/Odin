from django.db import models

class WhatsAppMessageLog(models.Model):
    sender_name = models.CharField("Nome do cliente", max_length=120, blank=True)
    sender_phone = models.CharField("Telefone", max_length=30, blank=True)
    incoming_text = models.TextField("Mensagem recebida")
    parsed_summary = models.TextField("Resumo interpretado", blank=True)
    generated_response = models.TextField("Resposta gerada", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Log WhatsApp"
        verbose_name_plural = "Logs WhatsApp"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.sender_name or self.sender_phone or 'Cliente'} - {self.created_at:%d/%m %H:%M}"
