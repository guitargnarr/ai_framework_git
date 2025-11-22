```typescript
File: app/components/PricingCard.tsx

'use client'

import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Badge } from '@/components/ui/badge'
import { CheckCircle2, Lock } from 'lucide-react'

interface PricingCardProps {
  tier: 'Basic' | 'Pro' | 'Enterprise'
}

export function PricingCard({ tier }: PricingCardProps) {
  const tiers = [
    { name: 'Basic', price: '$10/mo', features: ['5 users', '2GB storage', 'Unlimited emails'] },
    { name: 'Pro', price: '$25/mo', features: ['10 users', '10GB storage', 'Unlimited emails', 'Priority support'], popular: true },
    { name: 'Enterprise', price: '$50/mo', features: ['Unlimited users', 'Unlimited storage', 'Unlimited emails', 'Priority support'] }
  ]

  const currentTier = tiers.find(t => t.name === tier)!

  return (
    <Card className="max-w-sm">
      <CardHeader>
        <CardTitle>{currentTier.name}</CardTitle>
        {currentTier.popular && <Badge variant="outline">Popular</Badge>}
      </CardHeader>
      <CardContent>
        <div className="flex items-baseline justify-between mb-4">
          <div className="text-2xl font-semibold">${currentTier.price}</div>
          <div>/mo</div>
        </div>
        <ul className="space-y-2 text-sm">
          {currentTier.features.map((feature, index) => (
            <li key={index} className="flex items-center gap-2">
              <CheckCircle2 size={16} />
              {feature}
            </li>
          ))}
        </ul>
      </CardContent>
      <CardFooter>
        <Button variant="outline">Sign up</Button>
      </CardFooter>
    </Card>
  )
}
```